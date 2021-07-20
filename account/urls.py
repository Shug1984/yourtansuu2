from django.urls import path
from .views import signup, loginview, homeview, logoutview, indexview, UserChangeView, PasswordChange, PasswordChangeDone
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path('user_registration/signup/',signup, name = 'signup'),
    path('user_registration/login/', loginview, name = 'original_login'),
    path('user_registration/logout/', logoutview, name = 'original_logout'),
    path('user_registration/userupdate/<int:pk>/', UserChangeView.as_view(), name = 'userupdate'),
    path('user_registration/userupdate_complete/', TemplateView.as_view(template_name = 'user_registration/userupdate_complete.html'), name='userupdate_complete'), 
    path('user_registration/change_password/<int:pk>/', PasswordChange.as_view(template_name= 'user_registration/change_password.html'), name = 'change_password'),
    path('user_registration/change_password_complete.html', PasswordChangeDone.as_view(template_name= 'user_registration/change_password_complete.html'), name='change_password_complete'),
    path('home/', homeview, name = 'home'),   
    path('index/', indexview, name = 'index'),
]

