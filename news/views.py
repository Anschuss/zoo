from django.shortcuts import render
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView
from .models import News


class NewsListView(ListView):
    model = News
    template_name = 'news/news_page.html'


class NewDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
