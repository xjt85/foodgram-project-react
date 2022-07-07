FROM python:3.8.5
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN bin/install
COPY . .
CMD gunicorn foodgram_backend.wsgi:application --bind 0.0.0.0:8000