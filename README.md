# Movie Recommendation System
## Movie Recommendation System using Collaborative Method (User - User similarity , Item-Item similarity)

```diff
@@ Technologies - ML, NLP, Matrix Factorization @@
@@ Prerequisites - Python, ML, NLP, Linear Algebra @@
@@ Domain - Entertainment @@

```

### About the Dataset
https://www.kaggle.com/rounakbanik/movie-recommender-systems/data

The dataset consists of  metadata for all 45,000 movies listed in the Full MovieLens Dataset. The dataset consists of movies released on or before July 2017. Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages.

This dataset consists of the following files:

**movies_metadata.csv:** The main Movies Metadata file. Contains information on 45,000 movies featured in the Full MovieLens dataset. Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.

**keywords.csv:** Contains the movie plot keywords for our MovieLens movies. Available in the form of a stringified JSON Object.

**credits.csv:** Consists of Cast and Crew Information for all our movies. Available in the form of a stringified JSON Object.

**links.csv:** The file that contains the TMDB and IMDB IDs of all the movies featured in the Full MovieLens dataset.

**links_small.csv:** Contains the TMDB and IMDB IDs of a small subset of 9,000 movies of the Full Dataset.

**ratings_small.csv:** The subset of 100,000 ratings from 700 users on 9,000 movies.

### Project Plan

1. Merging all the given datasets ( credits.csv, keywords.csv, links.csv,links_small.csv,movies_metadata.csv,ratings_small.csv)

     ○ credits and keywords, credits and movies_metadata on id
     
     ○ ratings_small and links on movieId
     
     ○ links and credits on tmdbId
    
2. Data cleaning

   ● Exploratory Data Analysis (Data Visualisations)
   
   ● Data Preprocessing
   
3. Save the Dataframe as csv file which will be used in Popularity, Content, Collaborative Based Recommendation systems

4. Model Building

   ○ Weighted Rating for Popularity based Recommendation systems
   
   ○ TF-IDF (term frequency - inverse document frequency) for Content Based Recommendation system
   
   ○ KNN (K Nearest Neighbors) for Collaborative Based Recommendation system
   
   ##  After analysing each model's pros and cons , we thought collaborative recommendation system is better overall !
   
5. Model Serialisation and DeSerialisation

6.  Deployment using Streamlit where we have to select or type the movie accordingly to render output on screen

# To see the interface of the app 

#### Like how it looked like on laptop and mobile resolutions

```diff
+ Go to Collaborative Final Images folder
 ```
[Click on this to see the pics of interface on laptop and mobile](https://github.com/komalreddy3/MovieRecommendationSystem/tree/0ea71f0e3baa489a37bd55bf82d464d699d4577b/Colloborative%20Final%20Images)
