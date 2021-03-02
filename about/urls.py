from django.urls import path
from .views import AboutTemplateView, ContactFormView

app_name = 'about'

urlpatterns = [
    path('', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact')
]
