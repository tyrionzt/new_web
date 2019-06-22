# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Item, Photo

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)