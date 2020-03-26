from ubuntu:18.04

MAINTAINER JacobTheBanana "jacob@banana.abay.cf"

RUN apt-get update -y && \
    apt-get install -y python3-pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
RUN wget -O model.joblib https://github.com/jacobthebanana/McGill-AI-Stereotyper/releases/download/1.0/clf_avg_rating_forest_10_trees_50_50.joblib

COPY app.py /app

ENV FLASK_APP=app.py
CMD ["python3", "-m", "flask run", "--host=0.0.0.0", "--port=8000"]

EXPOSE 8000/tcp