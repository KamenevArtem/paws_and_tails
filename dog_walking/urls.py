from django.urls import path
from .views import index, show_cards


urlpatterns = [
    path('', index, name='index'),
    path('customers', show_cards)
]
