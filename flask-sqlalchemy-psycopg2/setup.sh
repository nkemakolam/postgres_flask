#!/bin/bash
virtualenv venv 
source venv/bin/activate 
pip install Flask
pip install Flask-SQLAlchemy 
pip install flask gunicorn 
pip install wheel 
pip install psycopg2 
python -m pip freeze > requirements.txt