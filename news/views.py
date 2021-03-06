from django.shortcuts import render
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import News
from .forms import *


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


## USER

class CreateUserView(CreateView):
    model = User
    form_class = RegistrationUserForm
    success_url = '/'
    template_name = 'news/registration.html'


class LoginUserView(LoginView):
    form_class = LoginUserForm
    success_url = '/'
    template_name = 'news/login.html'

class LogoutUser(LogoutView):
    pass
