import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""Load the Dataset"""

data = pd.read_csv(r"dataset.csv", encoding="latin-1")

data.head()

"""Get Data info"""

data.info()

data.describe()

"""# **Data Clean Up**

1.   Check for Duplicated data, and drop duplicates
2.   Check for Null data, and drop Null
"""

if data.duplicated().sum() > 0:
    print("There are duplicated data")
    data.drop_duplicates(inplace=True)
else:
    print("There is no duplicated data")

if data.isnull().sum().sum() > 0:
    print("There are null data")
    data.fillna("0", inplace=True)
else:
    print("There is no null data")

# prompt: Delete the NaN columns

data.dropna(axis=1, inplace=True)

data.columns

# prompt: delete these columns  'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
#        'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19',
#        'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23',
#        'Unnamed: 24', 'Unnamed: 25'

data.drop(
    [
        "Unnamed: 12",
        "Unnamed: 13",
        "Unnamed: 14",
        "Unnamed: 15",
        "Unnamed: 16",
        "Unnamed: 17",
        "Unnamed: 18",
        "Unnamed: 19",
        "Unnamed: 20",
        "Unnamed: 21",
        "Unnamed: 22",
        "Unnamed: 23",
        "Unnamed: 24",
        "Unnamed: 25",
    ],
    axis=1,
    inplace=True,
)

data.head()

"""# **Data Analysis**

1.   Segmentation typs into Movies and TV shows
2.   Check the best movie and TV show
"""

type_movie = data[data["type"] == "Movie"]
type_tv = data[data["type"] == "TV Show"]

number_of_movies = type_movie.count()[0]
number_of_tv = len(type_tv)
print("Number of Movies: ", number_of_movies)
print("Number of TV Shows: ", number_of_tv)

# 1. Analyze the distribution of movie and TV show ratings
data["rating"].value_counts().plot(kind="bar")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.title("Distribution of Movie and TV Show Ratings")
plt.show()

# 2. Analyze the relationship between release year and rating
sns.scatterplot(data=data, x="release_year", y="rating")
plt.xlabel("Release Year")
plt.ylabel("Rating")
plt.title("Relationship between Release Year and Rating")
plt.show()

# 3. Analyze the most popular genres
data["listed_in"].value_counts().head(10).plot(kind="bar")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.title("Most Popular Genres")
plt.show()

# 4. Analyze the relationship between duration and rating
sns.scatterplot(data=data, x="duration", y="rating")
plt.xlabel("Duration")
plt.ylabel("Rating")
plt.title("Relationship between Duration and Rating")
plt.show()

# 5. Analyze the relationship between duration and rating
sns.scatterplot(data=data, x="duration", y="rating")
plt.xlabel("Duration")
plt.ylabel("Rating")
plt.title("Relationship between Duration and Rating")
plt.show()
