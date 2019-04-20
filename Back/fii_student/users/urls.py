from django.urls import path
from django.conf.urls import url
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('activation_email_sent/', account_activation_sent, name='account_activation_sent'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
