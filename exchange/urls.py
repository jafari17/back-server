from django.urls import path

from . import views

urlpatterns = [
    path("lastPriceApi", views.LastPriceApi.as_view()),
]