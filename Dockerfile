from ubuntu:18.04

MAINTAINER JacobTheBanana "jacob@banana.abay.cf"

RUN apt-get update -y && \
    apt-get install -y python3-pip

RUN apt-get install -y wget

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt
RUN wget -O model-version-2.joblib https://github.com/jacobthebanana/McGill-AI-Stereotyper/releases/download/2.0/clf_avg_rating_forest_10_trees_50_50-scalar-categories.joblib

ARG CACHEBUST=1
COPY app.py /app

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=app.py

ENTRYPOINT ["python3"]
CMD ["app.py"]

EXPOSE 8000/tcp