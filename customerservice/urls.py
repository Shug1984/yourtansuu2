from django.urls import path
from .views import inquiryformview,InquiryCompleteView

urlpatterns = [
    path('inquiry-form/', inquiryformview, name = 'inquiry_form'),
    path('inquiry-complete/', InquiryCompleteView, name = 'inquiry_complete'),    
]
    
