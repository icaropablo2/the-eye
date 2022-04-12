setup:
	virtualenv -p python3 .venv

install:
	.venv/bin/pip install requirements.txt

run:
	.venv/bin/python manage.py runserver
