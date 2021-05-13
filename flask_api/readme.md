### BUilding Flask app using pipenv
Here are the step by step way to build a simple api with flask
We are using the 
### steps and command

pip install pipenv
pipenv shell 
pipenv install flash flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
pipenv install psycopg2-binary (https://github.com/pypa/pipenv/issues/3991)
pip freeze > requirements.txt
pipenv --rm (to purge the pipenv not that pipenv uses a different c++ lib for compiling from pip)

## for database read the documentation 
https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/# api_flask_heroku
