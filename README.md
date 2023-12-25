# Review_EZ

This project focuses on scraping reviews from an Amazon product link and generating a word cloud visual representation of these reviews. The system includes both frontend and backend components to present a word cloud visualization in a new window, aiming to provide users with a quick overview of product sentiment without needing to read through individual reviews.

## Purpose

The primary goal of this project is to streamline the process of understanding product sentiments by visually representing Amazon product reviews. By utilizing a word cloud, users can quickly grasp the most frequently mentioned keywords and sentiments related to a specific product.

## Features

- Scrapes reviews from an Amazon product link.
- Generates a word cloud based on the extracted reviews.
- Utilizes NLTK for keyword extraction and the RAKE model for efficient keyword processing.
- Frontend and Backend developed using React, Node.js, and FastAPI.

## Target Audience

This project caters to consumers interested in quickly understanding the overall sentiment and key aspects of a product on Amazon without going through extensive reviews.

## Technical Details

- Docker is required for the project.
- BeautifulSoup for scraping reviews from the Amazon product page into an Excel file.
- Utilizes NLTK for keyword extraction and Pandas along with the re library for pre-processing CSV files containing extracted reviews.
- FastAPI is used to integrate the WordCloud generation functionality into the backend.
- Uvicorn is utilized to enable FastAPI functionality.

## Installation and Usage

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IIIIIGODIIIII/Review_EZ.git)https://github.com/IIIIIGODIIIII/Review_EZ.git
   cd Review_EZ

2. Ensure you have Docker installed for project execution.

3. To install the dependencies for BackEnd and FrontEnd just cd to their directory and type:

   ```terminal 
      npm install

The above method will install all the depenencies for FrontEnd and BackEnd

4. Required Python Packages

   ```terminal
      pip install nltk rake-nltk uvicorn fastapi pandas beautifulsoup4 wordcloud 
   
### Usage

1. Create a Docker Container and start it.
   
2. Run the frontend and backend servers:

   ```terminal
   # Start backend server
   cd BackEnd
   nodemon index.js
   
   # Start frontend server
   cd FrontEnd
   npm start

Do these step in 2 different terminal windows

3. Execute FastAPI Integration.py in another terminal window
   
   ```python
   python FastAPI Integration.py

4. After following the above steps a new window will open which will ask the link for amazon product for which the wordcloud is to be generated, Just paste the product link and click Generate Image Button.

5. Wait for 30-45 seconds and a wordcloud will be generated 

## Additional Information 

### Future Plans 

Future updates may include:

- Implementation of multi-threading to enhance scraping speed.
- Support for multiple e-commerce platforms besides Amazon.
- Enhanced visualization options or sentiment analysis features.
