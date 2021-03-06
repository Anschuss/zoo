from django.urls import path
from .views import NewsListView, NewDetailView, NewsCreatView, \
    UpdateNewsView, DeleteNewsView, CreateUserView, \
    LoginUserView, LogoutUser

app_name = 'news'

urlpatterns = [
    ## News
    path('', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewDetailView.as_view(), name='detail'),
    path('news/create', NewsCreatView.as_view(), name='create'),
    path('news/update/<int:pk>', UpdateNewsView.as_view(), name = 'update'),
    path('news/delete/<int:pk>', DeleteNewsView.as_view(), name = 'delete'),
    ## User
    path('registration/', CreateUserView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout')
]