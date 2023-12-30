run:
	uvicorn app.main:app --reload


init: 
	cd app/ && alembic init migrations 

makemigrations:
	alembic revision --autogenerate

migrate: 
	alembic upgrade head

down:
	alembic downgrade -1


# shell:
# 	python manage.py shell

# makemigrations:
# 	python manage.py makemigrations

# migrate: makemigrations
# 	python manage.py migrate

# su:
# 	python manage.py createsuperuser