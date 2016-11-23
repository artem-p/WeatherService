FROM python:3.5
COPY . src/weatherservice
WORKDIR src/weatherservice
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.wsgi:app"]
