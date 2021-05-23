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
	pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d postgres latest.dump

sass:
	python manage.py sass holistic/static/css/style.scss holistic/static/css/style.css  -g

watch_sass:
	python manage.py sass holistic/static/css/style.scss holistic/static/css/style.css  --watch
