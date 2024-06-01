from django.urls import path

from . import views

urlpatterns = [
    path("route1/", views.matches_played_per_year, name="rout1"),
    path("route2/", views.matches_won_per_team_per_year, name="rout12"),
    path("route3/", views.extra_run_conceded_2016, name="rout3"),
    path("route4/", views.top_10_economical_bowler_2015, name="rout4"),

]
