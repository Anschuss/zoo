from django.urls import path
from .views import NewsListView, NewDetailView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewDetailView.as_view(), name='detail')
]