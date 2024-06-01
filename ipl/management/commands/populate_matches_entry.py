from django.core.management.base import BaseCommand
from django.db import transaction
from ipl.models import MatchesEntry
import csv as csv_module


class Command(BaseCommand):
    def import_csv(self, filename):
        print("populating MatchesEntry.......")
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv_module.DictReader(file)
            # atomic transaction
            with transaction.atomic():
                for row in reader:
                    MatchesEntry.objects.create(
                        # ID=int(row['id']),
                        season=row['season'],
                        city=row['city'],
                        date=row['date'],
                        team1=row['team1'],
                        team2=row['team2'],
                        toss_winner=row['toss_winner'],
                        toss_decision=row['toss_decision'],
                        result=row['result'],
                        dl_applied=bool(row['dl_applied']),
                        winner=row['winner'],
                        win_by_runs=int(row['win_by_runs']),
                        win_by_wickets=int(row['win_by_wickets']),
                        player_of_match=row['player_of_match'],
                        venue=row['venue'],
                        umpire1=row['umpire1'],
                        umpire2=row['umpire2'],
                        umpire3=row['umpire3']
                    )
        print("Done")

    def handle(self, *args, **options):
        self.import_csv('matches.csv')

