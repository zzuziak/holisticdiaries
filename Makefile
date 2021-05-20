db_migrate:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver


shell:
	python manage.py shell


dbshell:
	python manage.py dbshell

dump:
	heroku pg:backups:capture
	heroku pg:backups:download

sass:
	python manage.py sass holistic/static/css/style.scss holistic/static/css/style.css  -g

watch_sass:
	python manage.py sass holistic/static/css/style.scss holistic/static/css/style.css  --watch
