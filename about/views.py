from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from .models import MessageInformation


class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'


class ContactFormView(FormView):
    template_name = 'about/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['text']

        message = MessageInformation(email=email, subject=subject, text=text)
        message.save()

        return super().form_valid(form)
