from django.urls import path
from .views import signup, index, login

urlpatterns = [
    path('signup/',signup, name = 'signup'),
    path('index/', index, name = 'index'),
    path('login/', login, name = 'login'),
]