from django.urls import path
from .views import signup, loginview, homeview, logoutview, indexview, UserChangeView

urlpatterns = [
    path('user_registration/signup/',signup, name = 'signup'),
    path('user_registration/login/', loginview, name = 'original_login'),
    path('user_registration/logout/', logoutview, name = 'original_logout'),
    path('user_registration/userupdate/', UserChangeView.as_view(), name = 'userupdate'),
    path('home/', homeview, name = 'home'),   
    path('index/', indexview, name = 'index'),
     
]

