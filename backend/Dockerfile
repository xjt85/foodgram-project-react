FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
# CMD gunicorn foodgram_backend.wsgi:application --bind 0.0.0.0:8000
CMD ["gunicorn", "foodgram_backend.wsgi:application", "--bind", "0:8000" ]