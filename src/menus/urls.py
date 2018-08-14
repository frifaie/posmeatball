from django.urls import path

from .views import MenuActiveView, MenuDetailView

app_name = 'menus'
urlpatterns = [
    path('', MenuActiveView.as_view(), name='list'),
    path('<slug:slug>', MenuDetailView.as_view(), name='detail'),
]