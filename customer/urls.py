from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='customer_home'),
    path('about/', views.about, name='customer_about'),
]
