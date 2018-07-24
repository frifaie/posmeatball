from django.contrib.auth import views
from django.urls import path, reverse_lazy

from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .views import RegisterUserView

#app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logged_out.html'), name='logout'), #next_page=reverse_lazy('login')), name='logout'),

    path('register/', RegisterUserView.as_view(), name='register'),

    path('password_change/',
         views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
         name='password_change'),
    path('password_change/done/',
         views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),

    path('password_reset/',
         views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]


