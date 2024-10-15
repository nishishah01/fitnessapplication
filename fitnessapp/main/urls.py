from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *
urlpatterns=[
   path('register/',RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
   path('profile/',UserProfileView.as_view(),name='profile'),
   path('verify/<uidb64>/<token>/', verify_email, name='verify_email'),
]