from django.urls import path
from .views import (ItemCreate, Itemlistview, Itemcompleteview, Itemdetailview, Itemdeleteview, Itemdeleteview_complete, Itemupdateview, 
ClosetCreateView, ClosetCreateCompleteView, ClosetListView, ClosetUpdateView, ClosetUpdateCompleteView, SeasonGateView, SeasonListHomeView, 
OccasionGateView, OccasionListHomeView, TestView
)


urlpatterns = [
    path('item-create/', ItemCreate, name = 'item_create'),
    path('item-list/', Itemlistview, name = 'item_list'),
    path('item-complete/', Itemcompleteview, name = 'item_complete'),
    path('item-detail/<int:pk>/', Itemdetailview, name = 'item_detail' ),
    path('item-delete/<int:pk>/', Itemdeleteview, name = 'item_delete'),
    path('item-delete-confirm/<int:pk>/', Itemdeleteview, name = 'item_delete_confirm'),
    path('item-delete_complete/', Itemdeleteview_complete, name = 'item_delete_complete'),
    path('item-update/<int:pk>/', Itemupdateview, name = 'item_update'),
    path('closet-create/', ClosetCreateView, name = 'closet_create'),
    path('closet-create-complete/', ClosetCreateCompleteView, name = 'closet_create_complete'),
    path('closet-list/', ClosetListView, name = 'closet_list'),
    path('closet-update/<int:pk>/', ClosetUpdateView, name = 'closet_update'),
    path('closet-update-complete/', ClosetUpdateCompleteView, name = 'closet_update_complete'),
    path('season-gate/', SeasonGateView, name = 'season_gate'),
    path('season-list_home/', SeasonListHomeView, name = 'season_list_home'),
    path('occasion-gate/', OccasionGateView, name = 'occasion_gate'),
    path('occasion-list-home/', OccasionListHomeView, name = 'occasion_list_home'),
    path('testview/', TestView, name = 'testview'),
    ] 