from celery import Celery
from datetime import timedelta
import logging
from apps.crontasks.settings import OnBoundSetUp

celery = Celery()

logger = logging.getLogger('apps.crontasks')


@celery.task(base=OnBoundSetUp, run_every=timedelta(seconds=240),
             options={}, relative=False)
def test_task_1():
    logger.warning('Execution de TEST I')


@celery.task(base=OnBoundSetUp, run_every=timedelta(seconds=120),
             options={}, relative=False)
def test_task_2():
    logger.error("Execution de TEST II le logger est en rouge car c'est une erreur")
