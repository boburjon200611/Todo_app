from django.contrib import admin
from django.urls import path

from todoapp.views import todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Todo/',todo ),
]