from django.core.management.base import BaseCommand
from django.db import transaction
from ipl.models import MatchesEntry, DeliveriesEntry
import csv as csv_module


class Command(BaseCommand):
    def import_csv(self, file_path):
        print("populating DeliveriesEntry.......")
        with open(file_path, 'r') as file:
            reader = csv_module.DictReader(file)
            with transaction.atomic():
                for row in reader:
                    # Convert match_id to MatchesEntry object
                    curr_match_id = int(row['match_id'])
                    match = MatchesEntry.objects.get(ID=curr_match_id)
                    
                    # Create DeliveriesEntry object
                    delivery = DeliveriesEntry(
                        match_id=match,
                        inning=int(row['inning']),
                        batting_team=row['batting_team'],
                        bowling_team=row['bowling_team'],
                        over=int(row['over']),
                        ball=int(row['ball']),
                        batsman=row['batsman'],
                        non_striker=row['non_striker'],
                        bowler=row['bowler'],
                        is_super_over=bool(row['is_super_over']),
                        wide_runs=int(row['wide_runs']),
                        bye_runs=int(row['bye_runs']),
                        legbye_runs=int(row['legbye_runs']),
                        noball_runs=int(row['noball_runs']),
                        penalty_runs=int(row['penalty_runs']),
                        batsman_runs=int(row['batsman_runs']),
                        extra_runs=int(row['extra_runs']),
                        total_runs=int(row['total_runs']),
                        player_dismissed=row['player_dismissed'],
                        dismissal_kind=row['dismissal_kind'],
                        fielder=row['fielder']
                    )
                    delivery.save()
            print("Done")

    def handle(self, *args, **options):
        self.import_csv('deliveries.csv')
