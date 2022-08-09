# myapp/management/commands/import_csv.py
import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./ingredients.csv', 'r', encoding='utf-8') as csv_file:
            data_reader = csv.reader(csv_file)
            for row in data_reader:
                ingr = Ingredient()
                ingr.name = row[0]
                ingr.measurement_unit = row[1]
                ingr.save()
        self.stdout.write('Created.')
