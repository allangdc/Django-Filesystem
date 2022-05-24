# Django-Filesystem

python3 -m venv .venv
source .venv/bin/activate

python manage.py makemigrations
python manage.py migrate

python manage.py loaddata data.json

python manage.py runserver