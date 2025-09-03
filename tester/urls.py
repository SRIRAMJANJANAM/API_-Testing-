from django.urls import path
from .views import api_tester

urlpatterns = [
    path('', api_tester, name='api_tester'),
]
