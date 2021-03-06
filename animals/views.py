from django.shortcuts import render
from .models import Animal
from django.views.generic import ListView, DetailView, \
    UpdateView, CreateView, FormView


class AnimalListView(ListView):
    model = Animal
    template_name = 'animals/index.html'

    def get_queryset(self):
        return Animal.objects.select_related('kind', 'kind__family')
