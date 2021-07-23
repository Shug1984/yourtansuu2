from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Closet
from .forms import ClosetForm, ClosetNewCreation

class ClosetCreateClass(CreateView):
    template_name = 'contents/closet_create.html'
    model = Closet
    form = ClosetNewCreation
    fields = ('data_id','item_type','season','occasion','item_name','item_color','item_brand','purchase_date','pricing','purchase_place','memo','favorite_level','item_importance')
    success_url = reverse_lazy('index')


def closetlistview(request):
    object_list = Closet.objects.all()
    return render(request, 'closet_list.html',{'object_list':object_list})


# Create your views here.
