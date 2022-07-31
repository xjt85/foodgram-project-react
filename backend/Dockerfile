FROM python:3.10-slim
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
CMD gunicorn foodgram_backend.wsgi:application --bind 0.0.0.0:8000