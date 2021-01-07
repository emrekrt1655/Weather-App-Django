from django.urls import path
from .views import index, city_delete

urlpatterns = [
    path('', index, name="home"),
    path('<int:id>/delete/', city_delete, name="delete")
]