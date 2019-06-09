# Lehman Linked

This web app is built using the Django web framework utilizing Boostrap, and PostgreSQL for the database.

This web app allows users to signup and login to thier profiles and update it.

Users also have the ability to view other user profiles.

## Requirements
* PostgreSQL 11. or higher
* pip (to install Django)
* Django `2.1`
* Python 3.7

## Installing Django using pip
```
pip install Django==2.1
```

## Database Setup
Open PostgreSQL in the terminal and type:
```sql
CREATE ROLE admin WITH LOGIN PASSWORD 'postgres';
CREATE DATABASE postgres;
GRANT ALL PRIVILEGES ON DATABASE postgres TO admin;
```

## Starting the project:
```
git clone https://github.com/Stephen8898/LehmanLinked-Project.git
cd LehmanLinked-Project/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Then visit __127.0.0.1:8000__ or __localhost:8000__ in a browser