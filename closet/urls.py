from django.urls import path
from .views import ClosetCreateClass, closetlistview

urlpatterns = [
    path('contents/closet_create/', ClosetCreateClass.as_view(), name = 'closet_create'),
    path('contents/closet_list/', closetlistview, name = 'closet_list'),

    ]