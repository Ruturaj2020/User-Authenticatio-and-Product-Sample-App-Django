from django.urls import path
from . import views

urlpatterns = [
    path('pro/', views.product, name='product'),
]