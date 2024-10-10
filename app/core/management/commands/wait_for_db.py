"""
Danjo command to wait for the database to be available.
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Danjo command to wait for the database.
    """

    def handle(self, *args, **options):
        # pass
        """
        Entrypoint For Command.
        """

        self.stdout.write('Waiting for Database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database Unavailable, Waiting 1 sec...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))