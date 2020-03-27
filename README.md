# [Predict-a-title!](https://jacobthebanana.github.io/McGill-AI-Stereotyper/)
Ever thought about making a movie or a TV series? What would be people’s response? Would the average rating of your movie beat the averge?

Provide a few details about your title and instantly obtain a break-down of your title's performance! Keep in mind that the prediction here is just a guess- albeit an educated one. Behind this prediction is the automated analysis of over **300,000 titles**.

Interested? This model can be access without writing any code on your side. Simply visit https://jacobthebanana.github.io/McGill-AI-Stereotyper/ and receive your predicitions.  

## Getting Started (from the daily IMDb datasets)
### Building this model in Google Colab:
#### Data Preprocessing
1. Import the data-preprocessing notebook into Colab: `https://raw.githubusercontent.com/jacobthebanana/McGill-AI-Stereotyper/master/notebooks/2020-MAIS-Project-%20Data%20Preprocessing.ipynb`.
2. Adjust details including where to save the processed dataframe.
3. Run the notebook in Colab. 

#### The model
1. Import the model notebook into Colab: `https://github.com/jacobthebanana/McGill-AI-Stereotyper/blob/master/notebooks/2020-MAIS-Project-%20Model.ipynb`.
2. Replace the `wget` line with the command for loading the dataset that you've just preeprocessed in the previous step. Adjust the number of predictors if necessary. (Default is 10.)
3. Run the notebook in Colab and profit. Make sure that you download the pickled model `joblib`.

### Setting up the Webapp (locally, without Docker)
1. Install the Python package [requirements](https://github.com/jacobthebanana/McGill-AI-Stereotyper/blob/master/webapp/src/requirements.txt) using `pip3`.
2. In your copy of [`app.py`](https://github.com/jacobthebanana/McGill-AI-Stereotyper/blob/master/webapp/src/app.py), load the model that you've just trained using `joblib`.
3. Start the Webapp. Try running `python3 app.py` in a shell or command line.

### Building the Docker container
1. Clone this repo. Move [`Dockerfile`](https://raw.githubusercontent.com/jacobthebanana/McGill-AI-Stereotyper/master/Dockerfile), [`webapp/src/app.py`](https://raw.githubusercontent.com/jacobthebanana/McGill-AI-Stereotyper/master/webapp/src/app.py), and [`webapp/src/requirements.txt`](https://raw.githubusercontent.com/jacobthebanana/McGill-AI-Stereotyper/master/webapp/src/requirements.txt) to the same directory.
2. Modify `Dockerfile`. Instead of downloading the model from Github releases, simply `COPY` the pickled model that you and name it as `model-version-2.joblib` under `/app` in the container.
3. Ask Docker to `build` this image and profit.

## Acknowledgements
### Dataset
This project is based on the [IMDb datasets](https://www.imdb.com/interfaces/), retrieved on 16 March 2020.

### Libraries
This project is based on Python 3 and is made possible with the help of the following libraries:
- Numpy and Pandas for data-processing.
- Scikit-Learn for the Random-Forest autoClassifier.
- Pickle and Joblib for transferrin Python objects between Jupyter Notebooks and machines.
- Flask for the minimalistic HTTP server that simply gets the job done.
- ELI5 for the pretty-looking explanation of the predictions.

### Infrastructure
The front-end is simply an HTML form embedded in a [markdown document](https://github.com/jacobthebanana/McGill-AI-Stereotyper/blob/master/docs/index.md).

The backend is packaged into a Docker container with reference to [instructions](https://runnable.com/docker/python/dockerize-your-flask-application) from Runnable. 

The Docker container behind this webapp is running on a Docker Host of the [McGill Science Computer TaskForce](https://ctf.science.mcgill.ca/blurbs/hosting.html). The server itself is presumably located in a secret room on the third floor of McGill's McConnell Engineering Building. More information about this setup can be found on the [technical page](https://jacobthebanana.github.io/McGill-AI-Stereotyper/technical).
