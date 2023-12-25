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
   git clone https://github.com/your_username/your_project.git
   cd your_project
