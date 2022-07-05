#!/bin/sh
source venv/bin/activate
gunicorn foodgram_backend.wsgi:application --bind 0.0.0.0:8000