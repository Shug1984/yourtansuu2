from django.urls import path
from .views import signup, loginview, homeview

urlpatterns = [
    path('signup/',signup, name = 'signup'),
    path('login/', loginview, name = 'login'),
    path('home/', homeview, name = 'home'),
]