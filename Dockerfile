FROM python:3.5
ADD . src/weatherservice
WORKDIR src/weatherservice
RUN pip install -r requirements.txt

