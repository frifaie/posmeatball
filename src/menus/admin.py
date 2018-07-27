from django.contrib import admin

from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug', 'price']
    class Meta:
        model = Menu


admin.site.register(Menu, MenuAdmin)