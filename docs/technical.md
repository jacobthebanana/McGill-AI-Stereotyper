# Overview
This Webapp predicts the performance of your movie/TV-show based on its analysis of over **300,000** IMDB titles.

## The Autoclassifier Model
These resource-intensive computations were performed in Google Colab.

### Pre-processing
(Check out the [notebook](https://github.com/jacobthebanana/McGill-AI-Stereotyper/blob/master/notebooks/2020-MAIS-Project-%20Data%20Preprocessing.ipynb).)

The input comes in multiple datasets. The first step to do is to load and merge them into a single dataframe.

The next step is to discard some of the unused features such as names and multilingual titles.

The notebook would then condense the actor, writer, and director data by taking the average rating for each of the actor. 
(Thanks to Li from the McGill AI society for the tip.) Entries where such data are unavailable were discarded.

The dataframe is then pickled and stored as [`titles-with-ratings.pkl`](https://github.com/jacobthebanana/McGill-AI-Stereotyper/releases/download/1.0/titles-with-ratings.pkl).

### Fitting
(Check out the [notebook](https://github.com/jacobthebanana/McGill-AI-Stereotyper/blob/master/notebooks/2020-MAIS-Project-%20Model.ipynb).)

The pickled dataset is loaded and further processed. The genre information is converted to a multi-label binary representation. 
The rating is split into two categories: below average and above average.

A 10-estimator random forest auto-classifer (from Scikit-Learn) is fitted onto the training dataset (more than 300,000 entries.) 
With only 10 estimators, the model achieved a test accuracy of around 75% while using around 500 MB or RAM. 
Adding 20 more estimators would improve the test accuracy by another 5% percent. 
However, doing so was deemed not worthwhile, 
for that would more than double the RAM requirement and make the model more costly to deploy to the cloud. 

The model is then dumped to a joblib file.

## The Webapp
### Frontend
The frontend of this Webapp is simply an HTML form embedded in a markdown document. 
That markdown document is then published using Github Pages.

### Backend
A Flask App listens for GET requests to the API address. Once a request arrives, the Flask app would scan through its arguments. 
The Webapp would fill in any missing blanks with default values, and beep (with a 400 status code) if some required value is missing.
The user input would be converted to a Pandas dataframe and fed into the autoclassifier. The output is parsed with Numpy.

Note that the model (in Joblib format) is loaded into RAM at the start of the backend server.

## Other practical stuff
### Reverse Proxy & SSL Gateway
An Apache2 (Ubuntu) web server acts as the SSL reverse proxy gateway for the backend. This gateway is hosted on Amazon Lightsail (proudly) in Montreal, Quebec, Canada.

### Containerization
The backend is turned into a Docker [image](https://hub.docker.com/r/jacobthebanana/movie-rfc-backend), such that deployment would be a breeze.
This image is currently deployed on a (virtualized) [McGill Science Computer Taskforce](https://ctf.science.mcgill.ca/) Docker host in the McConnell Engineering Building of McGill University, Montreal, Quebec, Canada.
