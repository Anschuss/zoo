from django.shortcuts import render
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import News
from .forms import CreateNews


class NewsListView(ListView):
    model = News
    template_name = 'news/news_page.html'


class NewDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'


class NewsCreatView(CreateView):
    model = News
    form_class = CreateNews
    template_name = 'news/create_news.html'
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class UpdateNewsView(UpdateView):
    model = News
    form_class = CreateNews
    template_name = 'news/update_news.html'
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class DeleteNewsView(DeleteView):
    model = News
    template_name = 'news/delete_confirm.html'
    success_url = '/'
