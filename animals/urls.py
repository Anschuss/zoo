from django.urls import path
from .views import AnimalListView

app_name = 'animals'

urlpatterns = [
    path('', AnimalListView.as_view(), name='index'),
]
