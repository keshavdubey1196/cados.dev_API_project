from django.core.management import BaseCommand
from base.models import Company


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Company.objects.all().delete()
