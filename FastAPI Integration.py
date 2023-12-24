import requests 
from bs4 import BeautifulSoup
import pandas as pd
import re
import nltk
import matplotlib
import matplotlib.pyplot as plt
import uvicorn
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from rake_nltk import Rake
from collections import defaultdict
from wordcloud import WordCloud 
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException

review_list = []
app = FastAPI()

@app.get("/work")
def work(url: str):
    print("Incoming URL:", url)

    def get_soup(url):
        r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
        
    def main_landing_page(url):
        x = get_soup(url)
        a_tag = x.find('a', attrs={'data-hook': 'see-all-reviews-link-foot', 'class': 'a-link-emphasis a-text-bold'})
        href = a_tag.get('href')

        head = 'https://www.amazon.in'
        all_reviews_link = head + href
        return all_reviews_link

    def get_reviews(soup):
        reviews = soup.find_all('div', {'data-hook': 'review'})

        try:
            for item in reviews:
                product = soup.title.text.replace('Amazon.in:Customer reviews:','').strip()

                title = item.find('a', {'data-hook': 'review-title'}).text.strip()

                rating = float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip())
                
                body= item.find('span', {'data-hook': 'review-body'}).text.strip()
            
                review = {'product': soup.title.text.replace('Amazon.in:Customer reviews:',''),
                    'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                    'rating': float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                    'body': item.find('span', {'data-hook': 'review-body'}).text.strip()
                    }
        
                review_list.append(review)
        except: 
            pass

    #url = 'https://www.amazon.in/Harry-Potter-ChildrenS-Paperback-Boxed/dp/1408856778/ref=sr_1_7?crid=GJT0QD53HZKD&keywords=harry+potter&qid=1700505174&sprefix=harry+pott%2Caps%2C271&sr=8-7'
    new = main_landing_page(url)
    new_var = new + '&pageNumber='

    for x in range(1, 5):
        temp = new_var + str(x)
        soup = get_soup(temp)
        get_reviews(soup)
        if not soup.find('li', {'class': 'a-disabled a-last'}):
            pass
        else:
            break

    df = pd.DataFrame(review_list)
    df.to_excel('Reviews.xlsx', index=False)

    readata = pd.read_excel('Reviews.xlsx')
    array = readata[['rating','body']].values.tolist()

    # converting the dataset into pandas dataframe
    data=pd.DataFrame(array, columns=['rating','text'])

    # calculating the ratings' count
    rating={1:0,2:0,3:0,4:0,5:0}
    rating_order=data['rating'].value_counts().to_dict()
    rating.update(rating_order)

    #filling the null values
    data['text'] = data['text'].fillna('')  # replace null values with empty string
    data['text'] = data['text'].apply(lambda x: '' if not isinstance(x, str) else x)  # replace non-string values with empty string

    # extracting keywords using RAKE
    r = Rake(min_length=3, max_length=4,stopwords=stopwords.words('english'),
        punctuations = [')','(',',',':','),',').','.'])
    def extract_keywords(text):
        r.extract_keywords_from_text(text)
        return r.get_ranked_phrases()

    data['keywords'] = data['text'].apply(extract_keywords)

    # cleaning the data
    def clean(text):
        text = re.sub('[^a-zA-Z0-9]', ' ', text) # Removes special characters  
        text = text.lower() # Converts to lowercase
        text = re.sub('\s+', ' ', text) # Remove extra whitespace
        return text

    data['Cleaned Reviews'] = data['text'].apply(clean)

    # Tokenization
    def tokenize_text(text):
        tokens = nltk.word_tokenize(text)
        return tokens

    # POS tagging
    def pos_tag(tokens):
        tagged_tokens = nltk.pos_tag(tokens)
        return tagged_tokens

    # Extracting keywords from the Cleaned Reviews such that the adjective is followed by a noun
    pos_dict = {'J': 'A'}
    
    def token_stop_adjectives(text):
        tags = pos_tag(tokenize_text(text))
        newlist = []
        for i in range(len(tags)-1):
            word, tag = tags[i]
            if word not in set(stopwords.words('english')) and tag[0] in pos_dict:
                if tags[i+1][1][0] == 'N':
                    newlist.append((word + ' ' + tags[i+1][0]))
            elif word not in set(stopwords.words('english')) and tag[0] not in pos_dict:
                continue
        return newlist
    data['POS tagged'] = data['Cleaned Reviews'].apply(token_stop_adjectives)

    sia=SentimentIntensityAnalyzer()

    # Performing Sentimental Analysis
    word_scores = defaultdict(list)

    # Calculating the sentiment scores for each word in each sentence
    for sentence in data['POS tagged']:
        for word in sentence:
            scores = sia.polarity_scores(word)
            word_scores[word].append(scores['compound'])

    for sentence in data['keywords']:
        for word in sentence:
            scores = sia.polarity_scores(word)
            word_scores[word].append(scores['compound'])

    # Sorting the words by compound score
    positive_words = sorted(word_scores, key=lambda w: max(word_scores[w]), reverse=True)[:50]
    negative_words = sorted(word_scores, key=lambda w: min(word_scores[w]))[:50]

    # Algorithm to calculate the number of positive and negative words to be returned on the basis of the Ratings
    pos={1: 10, 2: 8, 3: 6, 4: 4,5: 2}
    neg={1: 2, 2: 4, 3: 6, 4: 8,5: 10}

    count_pos=0
    count_neg=0

    for key in rating:
        count_pos += round(rating[key]/pos[key])
        count_neg += round(rating[key]/neg[key])

    # Generating an array of product's features
    p=0
    n=0
    returnwords=[]
    for word in positive_words:
        if(p<count_pos and max(word_scores[word])>0.5 ):
            returnwords.append({'text':clean(word), 'value':round(max(word_scores[word])*100,2)})
            p=p+1
        else:
            break

    for word in negative_words:
        if(n<count_neg):
            returnwords.append({'text':clean(word), 'value':round(min(word_scores[word])*100,2)})
            n=n+1
        else:
            break        
            
    returnwords

    # Create a string containing all the words
    font_path = 'E:\Computer Science\Machine Learning\Projects\ReviewEZ\Font\static\Quicksand-Regular.ttf'
    text = ' '.join(word['text'] for word in returnwords)

    # Generate the word cloud
    wordcloud = WordCloud(font_path, width=800, height=600, background_color='white').generate(text)

    # Saving and returning the image
    matplotlib.use('Agg')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    file_path = 'E:\Computer Science\Machine Learning\Projects\ReviewEZ\WordCloud\WordCloud.png'
    plt.savefig(file_path, format='png')
    plt.close()

    return FileResponse(file_path)
    #return FileResponse(file_path, media_type="image/png")

if __name__ == "__main__":
    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
