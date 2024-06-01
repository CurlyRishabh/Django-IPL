from django.core.management.base import BaseCommand
from django.db import transaction
from ipl.models import MatchesEntry, DeliveriesEntry



class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Deleting all entry....")
        with transaction.atomic():
            MatchesEntry.objects.all().delete()
            DeliveriesEntry.objects.all().delete()

        print("Deleting done.")