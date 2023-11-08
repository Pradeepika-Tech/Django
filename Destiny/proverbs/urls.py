from django.urls import path
from .views import first_proverb_view

urlpatterns = [
    path('', first_proverb_view),
]