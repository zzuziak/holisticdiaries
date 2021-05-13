db_migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver


shell:
	python manage.py shell


dbshell:
	python manage.py dbshell