db_migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver


shell:
	python manage.py shell


dbshell:
	python manage.py dbshell

sass:
	python manage.py sass holistic/static/css/style.scss holistic/static/css/style.css  -g
