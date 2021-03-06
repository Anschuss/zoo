from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm
from celery import current_app
from .task import save_user_message


class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'


class ContactFormView(LoginRequiredMixin, FormView):
    template_name = 'about/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        text = form.cleaned_data['text']

        save_user_message.delay(email, subject, text)

        return super().form_valid(form)
