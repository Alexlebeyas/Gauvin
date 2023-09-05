import logging
from datetime import timedelta

from apps.crontasks.settings import OnBoundSetUp
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
from django.db import connections
from django.utils.translation import gettext_lazy as _

celery = Celery()

logger = logging.getLogger('apps.crontasks')


@celery.task(base=OnBoundSetUp, run_every=timedelta(minutes=settings.CRON_SHEDULE_FOR_DB_CONNECTION_TEST), options={},
             relative=False)
def check_db_connection():
    """
     It is used to check database availability. each time he launches in tries
     to connect to the database a certain number of times calls the function
     below with the number of successful connections
    :return None:
    """
    if settings.IS_DB_CONNECTION_SHOULD_TEST:
        logger.warning(_("Can RUN"))
        logger.warning(f"{settings.CRON_NB_TEST_FOR_DB_CONNECTION} numers of runs")
        db_conn = connections['default']
        success = 0
        for i in range(settings.CRON_NB_TEST_FOR_DB_CONNECTION):
            logger.warning(f"{i} Run time")
            try:
                db_conn.cursor()
            except Exception as e:
                logger.error(_("Database connection failure"))
                logger.error(f"{e}")
            else:
                success += 1
                logger.info(_("Database connection success"))
            logger.warning(f"{success} Success value")
        handle_test_db_connection_result(success)


def handle_test_db_connection_result(success: int):
    """
    From the number of successful connections to the database, we validate the
    availability of the database. If it is not good, we send an email to the
    admin configured in the settings
    :param success:
    :return:
    """
    success_percent = success * 100 / settings.CRON_NB_TEST_FOR_DB_CONNECTION
    if success_percent < settings.CRON_PERCENT_APPROVE_FOR_DB_CONNECTION:
        send_mail(
            _("Database connection failure"),
            f"IConnection to the database is no longer possible.\n "
            f"The percentage of success is {success_percent}",
            f"{settings.ADMINS[0][0]}",
            [f"{settings.ADMINS[0][0]}"],
            fail_silently=False,
        )
