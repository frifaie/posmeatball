from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.utils.http import is_safe_url
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

from .forms import ContactForm

# def home_page(request):
#     return render(request, "home_page.html", {})

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = './'

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        context['content'] = 'Send us your message'
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ContactFormView, self).form_valid(form)



#
# class LoginView(FormView):
#     template_name = 'auth/login.html'
#     form_class = AuthenticationForm
#     success_url = '/'
#     redirect_field_name = REDIRECT_FIELD_NAME
#
#     def get_context_data(self, **kwargs):
#         context = super(LoginView, self).get_context_data(**kwargs)
#         context['title'] = 'Please Login'
#         return context
#
#     @method_decorator(sensitive_post_parameters('password'))
#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, request, *args, **kwargs):
#         request.session.set_test_cookie()
#         return super(LoginView, self).dispatch(request, *args, **kwargs)
#
#     def form_valid(self, form):
#         auth_login(self.request, form.get_user())
#         if self.request.session.test_cookie_worked():
#             self.request.session.delete_test_cookie()
#         return super(LoginView, self).form_valid(form)
#
#     def get_success_url(self):
#         redirect_to = self.request.GET.get(self.redirect_field_name)
#         if not is_safe_url(url=redirect_to, host=self.request.get_host()):
#             redirect_to = self.success_url
#         return redirect_to
#
#
# class LogoutView(RedirectView):
#     url = '/login/'
#
#     def get(self, request, *args, **kwargs):
#         auth_logout(request)
#         return super(LogoutView, self).get(request, *args, **kwargs)
#
