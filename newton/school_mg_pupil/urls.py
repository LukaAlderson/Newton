from django.urls import path
from . import views

urlpatterns = [
    path("", views.pupil_profile, name="pupil_profile"),
]
