from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Closet
from .forms import ClosetForm

@login_required
def ClosetCreate(request):
    if request.method == 'POST':
        form = ClosetForm(request.POST)
        if form.is_valid():
            action = request.POST['action']
            if action == 'input':
                return render(request, 'contents/closet_create.html', {'form':form})
            elif action == 'confirm':
                return render(request, 'contents/closet_confirm.html', {'form':form})
            else:
                closet = form.save(commit=False)
                closet.user_id = request.user
                closet.save()
                return redirect('closet_complete')
    else:
        form = ClosetForm()
    return render(request,'contents/closet_create.html', {'form':form})


@login_required
def closet_completeview(request):
    return render(request, 'contents/closet_complete.html')
    
@login_required
def closetlistview(request):
    object_list = Closet.objects.filter(user_id = request.user)
    return render(request, 'contents/closet_list.html',{'object_list':object_list})

@login_required
def closetdetailview(request, pk):
    object_list = Closet.objects.filter(user_id = request.user, pk=pk)
    return render(request, 'contents/closet_detail.html',{'object_list':object_list})



# Create your views here.
