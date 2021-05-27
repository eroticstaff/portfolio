from django.urls import path
from .views import index
app_name = 'organizer'
urlpatterns = [
    path('', index, name="index"),
]