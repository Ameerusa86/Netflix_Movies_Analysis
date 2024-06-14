# Netflix Titles Analysis

This repository contains a data analysis project on the Netflix titles dataset. The project includes data cleaning, segmentation, and various analyses to extract insights from the dataset. The dataset is sourced from [Kaggle](https://www.kaggle.com/shivamb/netflix-shows).

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Analysis](#analysis)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to analyze a Netflix titles dataset to understand various aspects such as the distribution of movie and TV show ratings, the relationship between release year and rating, the most popular genres, and the relationship between duration and rating.

## Dataset

The dataset contains information about movies and TV shows available on Netflix as of 2021. The key attributes in the dataset include:

- `show_id`: Unique ID for each show
- `type`: Type of content (Movie or TV Show)
- `title`: Title of the content
- `director`: Director of the content
- `cast`: Cast of the content
- `country`: Country of origin
- `date_added`: Date the content was added to Netflix
- `release_year`: Release year of the content
- `rating`: Rating of the content
- `duration`: Duration of the content (minutes for movies, seasons for TV shows)
- `listed_in`: Genre of the content
- `description`: Description of the content

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/netflix-titles-analysis.git

2. Navigate to the project directory:

   ```bash
   cd Netflix-Movies-Analysis

3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

4. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage
1. Ensure the dataset (netflix_titles.csv) is in the project directory.
2. Run the analysis script:
   ```bash
   python main.py

The script will perform data cleaning, segmentation, and various analyses, producing visualizations of the results.

## Analysis
The analysis includes the following steps:

1. Data Cleaning:
  - Remove duplicate entries
  - Handle missing values
  - Drop unnecessary columns
    
2. Segmentation:
  - Segment data into Movies and TV Shows
  - Count the number of Movies and TV Shows

3. Visual Analysis:
  - Distribution of movie and TV show ratings
  - Relationship between release year and rating
  - Most popular genres
  - Relationship between duration and rating
