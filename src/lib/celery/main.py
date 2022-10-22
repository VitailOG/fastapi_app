from celery import Celery

from src.config import settings

#  check que
app = Celery(
    'tasks',
    backend=settings.CELERY_BACKEND_URL,
    broker=settings.CELERY_BROKER_URL
)
