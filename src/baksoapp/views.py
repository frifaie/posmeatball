from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.views.generic import TemplateView, FormView

from .forms import ContactForm

# def home_page(request):
#     return render(request, "home_page.html", {})

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = './'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['title']    = 'Contact Us'
        context['content']  = 'Send us your message'
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ContactFormView, self).form_valid(form)