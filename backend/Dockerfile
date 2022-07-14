FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "foodgram_backend.wsgi:application", "--bind", "0:8000" ]
