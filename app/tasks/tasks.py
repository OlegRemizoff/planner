from app.tasks.celery import celery


# celery -A app.tasks.celery:celery worker --loglevel=INFO

@celery.task
def add(x, y):
    return f"\nВсе работает {x + y}"


add.delay(10, 20)