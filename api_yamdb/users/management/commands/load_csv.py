import csv
import os

from django.core.management.base import BaseCommand
from users.models import User
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_dir = os.path.join(settings.BASE_DIR, 'static/data/')
        with open(data_dir + 'users.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name']
                )
                record.save()
        print('csv files loading completed.')
