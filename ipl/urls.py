from django.urls import path

from . import views

urlpatterns = [
    path("route1/", views.matches_played_per_year, name="rout1"),
    path("route2/", views.matches_won_per_team_per_year, name="rout12"),
    path("route3/", views.extra_run_conceded_2016, name="rout3"),
    path("route4/", views.top_10_economical_bowler_2015, name="rout4"),
    path("chart1/", views.chart1, name="chart1"),
    path("chart2/", views.chart2, name="chart2"),
    path("chart3/", views.chart3, name="chart3"),
    path("chart4/", views.chart4, name="chart3"),
    path("chart5/", views.chart5, name="chart5"),
]
