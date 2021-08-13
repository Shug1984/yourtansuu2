from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Closet
from .forms import ClosetForm

@login_required
def ClosetCreate(request):
    if request.method == 'POST':
        form = ClosetForm(request.POST, request.FILES)
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
    #object_item = Closet.objects.filter(user_id = request.user, pk=pk)
    object_item = Closet.objects.get(user_id = request.user, pk=pk)
    return render(request, 'contents/closet_detail.html',{'object_item':object_item})

@login_required
def closetdeleteview(request, pk):
    object_item = Closet.objects.filter(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button', '') == 'confirm':
            return render(request, 'contents/closet_delete_confirm.html', {'object_item':object_item})
        else:
            object_item.delete()
        return redirect('closet_delete_complete')

    else:
        return render(request, 'contents/closet_delete.html',{'object_item':object_item})

@login_required
def closetdeleteview_complete(request):
    return render(request, 'contents/closet_delete_complete.html')   

@login_required
def closetupdateview(request, pk):
    object_item = Closet.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ClosetForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('closet_detail', pk=pk)
    else:
        form = ClosetForm(instance = object_item)
    return render(request, 'contents/closet_update.html',{'form':form, 'object_item':object_item})


def closetlisting(request):
    closet_list = Closet.objects.filter(user_id = request.user)
    paginator = Paginator(closet_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/paginator.html', {'page_object': page_object})



