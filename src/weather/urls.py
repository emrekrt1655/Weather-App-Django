from django.urls import path
from .views import index, city_delete

urlpatterns = [
    path('', index, name="home"),
    path('<name>/delete/', city_delete, name="delete")
]