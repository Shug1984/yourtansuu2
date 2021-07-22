from django.urls import path
from .views import ClosetCreateClass

urlpatterns = [
    path('contents/closet_create/', ClosetCreateClass.as_view(), name = 'closet_create'),
    ]