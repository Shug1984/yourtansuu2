from django.urls import path
from .views import signup, loginview, homeview, logoutview, indexview, UserChangeView, PasswordChange, PasswordChangeDone,PasswordReset, PasswordResetDone, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete, userinfoview, accountcontrolview
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('user-registration/signup/',signup, name = 'signup'),
    path('user-registration/login/', loginview, name = 'original_login'),
    path('user-registration/logout/', logoutview, name = 'original_logout'),
    path('user-registration/userinformation/<int:pk>/', userinfoview, name = 'user_information'),
    path('user-registration/userupdate/<int:pk>/', UserChangeView.as_view(), name = 'userupdate'),
    path('user-registration/userupdate-complete/', TemplateView.as_view(template_name = 'user_registration/userupdate_complete.html'), name='userupdate_complete'), 
    path('user-registration/change-password/<int:pk>/', PasswordChange.as_view(template_name= 'user_registration/change_password.html'), name = 'change_password'),
    path('user-registration/change-password-complete', PasswordChangeDone.as_view(template_name= 'user_registration/change_password_complete.html'), name='change_password_complete'),
    path('user-registration/reset-password/', PasswordReset.as_view(template_name ='user_registration/reset_password.html'), name = 'reset_password'),
    path('user-registration/reset-password-complete/', PasswordResetDone.as_view(template_name ='user_registration/reset_password_complete.html'), name = 'reset_password_complete'),
    path('user-registration/reset-password-confirm/', PasswordResetConfirm.as_view(template_name ='user_registration/reset_password_confirm.html'), name = 'reset_password_confirm'),
    path('user-registration/reset-password-finish/', PasswordResetComplete.as_view(template_name ='user_registration/reset_password_finish.html'), name = 'reset_password_finish'),
    path('home/', homeview, name = 'home'),   
    path('index/', indexview, name = 'index'),
    path('accountcontrol/', accountcontrolview, name = 'account_control'),
] 

