from django.urls import path
from .views import ClosetCreate, closetlistview, closet_completeview, closetdetailview, closetdeleteview

urlpatterns = [
    path('contents/closet_create/', ClosetCreate, name = 'closet_create'),
    path('contents/closet_list/', closetlistview, name = 'closet_list'),
    path('contents/closet_complete/', closet_completeview, name = 'closet_complete'),
    path('contents/closet_detail/<int:pk>/', closetdetailview, name = 'closet_detail' ),
    path('contents/closet_delete/<int:pk>/', closetdeleteview, name = 'closet_delete'),
    ]