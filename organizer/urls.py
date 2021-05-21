from django.urls import path

from .views import index, save_card

app_name = 'organizer'
urlpatterns = [
    path('', index, name="index"),
    path('save', save_card, name="save")
]