# myapp/management/commands/import_csv.py
import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredient


class Command(BaseCommand):
    def handle(self, *args, **options):
        data_reader = csv.reader(open('../data/ingredients.csv'), delimiter=',', quotechar='"')
        for row in data_reader:
            ingr = Ingredient()
            ingr.name = row[0]
            ingr.measurement_unit = row[1]
            ingr.save()
        self.stdout.write('Created.')
