from django.urls import path
from .views import index

urlpatterns = [
    path('', index.html, name="home")
]