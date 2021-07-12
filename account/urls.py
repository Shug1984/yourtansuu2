from django.urls import path
from .views import signup, loginview, homeview, logoutview

urlpatterns = [
    path('signup/',signup, name = 'signup'),
    path('login/', loginview, name = 'login'),
    path('logout/', logoutview, name = 'logout'),
    path('home/', homeview, name = 'home'),    
]