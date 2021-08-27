from django.urls import path
from .views import (topview, signup, loginview, logoutview, UserChangeView, homeview,
PasswordChange, PasswordChangeDone,PasswordReset, PasswordResetDone, PasswordResetDone, PasswordResetConfirm, PasswordResetComplete, 
userinfoview, usercontrolview, testview
)
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('signup/',signup, name = 'signup'),
    path('login/', loginview, name = 'login'),
    path('logout/', logoutview, name = 'logout'),
    path('userinformation/<int:pk>/', userinfoview, name = 'user_information'),
    path('userupdate/<int:pk>/', UserChangeView.as_view(), name = 'user_update'),
    path('userupdate-complete/', TemplateView.as_view(template_name = 'account/user_update_complete.html'), name='user_update_complete'), 
    path('change-password/<int:pk>/', PasswordChange.as_view(template_name= 'account/change_password.html'), name = 'change_password'),
    path('change-password-complete', PasswordChangeDone.as_view(template_name= 'account/change_password_complete.html'), name='change_password_complete'),
    path('reset-password/', PasswordReset.as_view(template_name ='account/reset_password.html'), name = 'reset_password'),
    path('reset-password-complete/', PasswordResetDone.as_view(template_name ='account/reset_password_complete.html'), name = 'reset_password_complete'),
    path('reset-password-confirm/', PasswordResetConfirm.as_view(template_name ='account/reset_password_confirm.html'), name = 'reset_password_confirm'),
    path('reset-password-finish/', PasswordResetComplete.as_view(template_name ='account/reset_password_finish.html'), name = 'reset_password_finish'),
    path('home/', homeview, name = 'home'),
    path('user-control/', usercontrolview, name = 'user_control'),
    path('bootstrap-test/', testview, name = 'testview'),
] 

