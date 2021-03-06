from django.shortcuts import render
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import News
from .forms import *
from django.contrib.auth.mixins import UserPassesTestMixin


class StaffOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class NewsListView(ListView):
    model = News
    template_name = 'news/news_page.html'


class NewDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'


class NewsCreatView(StaffOnlyMixin, CreateView):
    model = News
    form_class = CreateNews
    template_name = 'news/create_news.html'
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class UpdateNewsView(StaffOnlyMixin, UpdateView):
    model = News
    form_class = CreateNews
    template_name = 'news/update_news.html'
    success_url = '/'

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super().form_valid(form)


class DeleteNewsView(StaffOnlyMixin, DeleteView):
    model = News
    template_name = 'news/delete_confirm.html'
    success_url = '/'


## USER
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView


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
