import random
import os

import itertools
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from django.utils.text import slugify


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename    = random.randint(999, 3999999999)
    name, ext       = get_filename_ext(filename)
    final_filename  = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "menus/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class MenuQuerySet(models.query.QuerySet):
    def meal(self):
        return self.filter(menu_type='meal')

    def drink(self):
        return self.filter(menu_type='drink')

    def snack(self):
        return self.filter(menu_type='snack')

    def active(self):
        return self.filter(active=True)

    def search(self, query):
        lookups = (Q(name__icontains=query)|
                   Q(description__icontains=query)|
                   Q(price__icontains=query)|
                   Q(menu_type__icontains=query)
                   )
        return self.filter(lookups).distinct()


class MenuManager(models.Manager):
    def get_queryset(self):
        return MenuQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def meal(self):
        return self.get_queryset().active().meal()

    def drink(self):
        return self.get_queryset().active().drink()

    def snack(self):
        return self.get_queryset().active().snack()

    def search(self, query):
        return self.get_queryset().active().search(query)


MENU_TYPE = (
    ('meal', 'Meal'),
    ('drink', 'Drink'),
    ('snack', 'Snack'),
)

class Menu(models.Model):
    name        = models.CharField(max_length=120)
    slug        = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=9999.99)
    image       = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    menu_type   = models.CharField(max_length=120, choices=MENU_TYPE)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = MenuManager()

    def get_absolute_url(self):\
        return reverse("menus:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


def menus_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = orig = slugify(instance.name)

        for x in itertools.count(1):
            if not Menu.objects.filter(slug=instance.slug).exists():
                break
            instance.slug ='{0}-{1}'.format(orig, x)


pre_save.connect(menus_pre_save_receiver, sender=Menu)



