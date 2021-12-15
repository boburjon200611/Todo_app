from django.contrib import admin
from .models import Todo
from django.contrib.admin import ModelAdmin

@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    search_fields = ['title',]
