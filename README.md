# Django-Filesystem

## Setup system

### Init virtual env
    python3 -m venv .venv
    source .venv/bin/activate

### Install requirement packages
    pip install -r requirements.txt

### Create database
    python manage.py makemigrations
    python manage.py migrate

### Insert initial data
    python manage.py loaddata data.json

### Start server
    python manage.py runserver
