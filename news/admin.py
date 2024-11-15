from django.contrib import admin
from .models import *
from .views import category


# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'image')

admin.site.register(New)
admin.site.register(Category)
admin.site.register(Region)