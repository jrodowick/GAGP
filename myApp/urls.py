from django.conf.urls import url
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path('^$', views.index, name = 'index'),
    path('register/', views.register, name = 'register'),
    path('locations/', views.locations, name = 'locations'),
    path('local_event/', views.local_event, name = 'local_event'),
    path('events/', views.events, name = 'events'),
    path('login/', auth_views.LoginView.as_view(template_name = 'index.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('about/', views.about, name = 'about'),
    path('profile/', views.profile, name = 'profile'),
]
