from django.urls import path

from . import views

app_name = "profiless"

urlpatterns = [
    path('profiles/', views.index, name='index'),
    path('profiles/<str:username>/', views.profile, name='profile'),
    ]
