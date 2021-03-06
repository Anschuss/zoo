from django.urls import path
from .views import NewsListView, NewDetailView, \
    NewsCreatView, UpdateNewsView, DeleteNewsView

app_name = 'news'

urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewDetailView.as_view(), name='detail'),
    path('news/create', NewsCreatView.as_view(), name='create'),
    path('news/update/<int:pk>', UpdateNewsView.as_view(), name = 'update'),
    path('news/delete/<int:pk>', DeleteNewsView.as_view(), name = 'delete'),
]