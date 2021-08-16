from django.urls import path
from .views import ItemCreate, Itemlistview, Itemcompleteview, Itemdetailview, Itemdeleteview, Itemdeleteview_complete, Itemupdateview, Itemlisting

urlpatterns = [
    path('contents/item-create/', ItemCreate, name = 'item_create'),
    path('contents/item-list/', Itemlistview, name = 'item_list'),
    path('contents/item-complete/', Itemcompleteview, name = 'item_complete'),
    path('contents/item-detail/<int:pk>/', Itemdetailview, name = 'item_detail' ),
    path('contents/item-delete/<int:pk>/', Itemdeleteview, name = 'item_delete'),
    path('contents/item-delete-confirm/<int:pk>/', Itemdeleteview, name = 'item_delete_confirm'),
    path('contents/item-delete_complete/', Itemdeleteview_complete, name = 'item_delete_complete'),
    path('contents/item-update/<int:pk>/', Itemupdateview, name = 'item_update'),
    path('contents/paginator-list/', Itemlisting, name = 'paginator'),
    ] 