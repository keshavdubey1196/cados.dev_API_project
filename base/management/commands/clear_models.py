from django.core.management import BaseCommand
from base.models import Advocate


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Advocate.objects.all().delete()
