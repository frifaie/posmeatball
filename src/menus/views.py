from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Menu



class MenuActiveView(ListView):
    template_name = "menus/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Menu.objects.all()


class MenuDetailView(DetailView):
    queryset = Menu.objects.all()
    template_name = "menus/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(MenuDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        pk = self.kwargs.get('pk')
        instance = Menu.objects.get(slug=slug, active=True)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance