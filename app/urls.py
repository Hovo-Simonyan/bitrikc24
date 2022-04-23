from django.urls import path
from .views import UrlCreate

urlpatterns = [
    path('', UrlCreate.as_view(), name='home'),
]