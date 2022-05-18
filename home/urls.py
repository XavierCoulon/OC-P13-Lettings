from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profiles', include('profiles.urls', namespace='profiles')),
    path('lettings', include('lettings.urls', namespace='lettings')),
    path('sentry-debug/', views.trigger_error),
]
