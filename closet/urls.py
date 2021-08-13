from django.urls import path
from .views import ClosetCreate, closetlistview, closet_completeview, closetdetailview, closetdeleteview, closetdeleteview_complete, closetupdateview, closetlisting

urlpatterns = [
    path('contents/closet-create/', ClosetCreate, name = 'closet_create'),
    path('contents/closet-list/', closetlistview, name = 'closet_list'),
    path('contents/closet-complete/', closet_completeview, name = 'closet_complete'),
    path('contents/closet-detail/<int:pk>/', closetdetailview, name = 'closet_detail' ),
    path('contents/closet-delete/<int:pk>/', closetdeleteview, name = 'closet_delete'),
    path('contents/closet-delete-confirm/<int:pk>/', closetdeleteview, name = 'closet_delete_confirm'),
    path('contents/closet-delete_complete/', closetdeleteview_complete, name = 'closet_delete_complete'),
    path('contents/closet-update/<int:pk>/', closetupdateview, name = 'closet_update'),
    path('contents/paginator-list/', closetlisting, name = 'paginator'),
    ] 