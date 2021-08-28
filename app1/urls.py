from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from products import views as v

urlpatterns = [
    path('', views.home, name='home'),
    path('login/app1/dashboard/',views.dashboard,name='dashboard'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('posting/', views.postview.as_view(), name='postview'),
    path('pro/',v.product,name='product')
]