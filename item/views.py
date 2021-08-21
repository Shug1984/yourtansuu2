from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Item, Closet
from .forms import ItemForm, ClosetForm


def decode_base64_file(file_name, data):
    from django.core.files.base import ContentFile
    import base64

    if 'data:' in data and ';base64,' in data:
        header, data = data.split(';base64,')

        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        return ContentFile(decoded_file, name=file_name)
    return None


@login_required
def ItemCreate(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            action = request.POST['action']
            if action == 'input':
                return render(request, 'contents/item_create.html', {'form':form})
            elif action == 'confirm':
                return render(
                    request,
                    'contents/item_confirm.html',
                    {
                        'form':form,
                        'item_image_base64': request.POST.get('item_image_base64'),
                    }
                )
            else:
                item = form.save(commit=False)
                item.item_image = decode_base64_file(
                    request.POST.get('item_image'),
                    request.POST.get('item_image_base64')
                )
                item.user = request.user
                item.save()
                return redirect('item_complete')
    else:
        form = ItemForm()
    return render(request,'contents/item_create.html', {'form':form})


@login_required
def Itemcompleteview(request):
    return render(request, 'contents/item_complete.html')
    
@login_required
def Itemlistview(request):
    item_list = Item.objects.filter(user_id = request.user)
    paginator = Paginator(item_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/item_list.html', {'page_object': page_object})

@login_required
def Itemdetailview(request, pk):
    #object_item = Closet.objects.filter(user_id = request.user, pk=pk)
    object_item = Item.objects.get(user_id = request.user, pk=pk)
    return render(request, 'contents/item_detail.html',{'object_item':object_item})

@login_required
def Itemdeleteview(request, pk):
    object_item = Item.objects.filter(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button', '') == 'confirm':
            return render(request, 'contents/item_delete_confirm.html', {'object_item':object_item})
        else:
            object_item.delete()
        return redirect('item_delete_complete')

    else:
        return render(request, 'contents/item_delete.html',{'object_item':object_item})

@login_required
def Itemdeleteview_complete(request):
    return render(request, 'contents/item_delete_complete.html')   

@login_required
def Itemupdateview(request, pk):
    object_item = Item.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ItemForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('item_detail', pk=pk)
    else:
        form = ItemForm(instance = object_item)
    return render(request, 'contents/item_update.html',{'form':form, 'object_item':object_item})

def ClosetCreateView(request):
    if request.method == 'POST':
        form = ClosetForm(request.POST)
        if form.is_valid():
            closet = form.save(commit=False)
            closet.user = request.user
            closet.save()
            return redirect('closet_create_complete')
    else:
        form = ClosetForm()
    return render(request,'contents/closet_create.html', {'form':form})

def ClosetCreateCompleteView(request):
    return render(request, 'contents/closet_create_complete.html')


def ClosetListView(request):
    object_list = Closet.objects.filter(user_id = request.user)
    return render(request, 'contents/closet_list.html', {'object_list':object_list})

"""
def ClosetDetailView(request):
    object_list = Item.objects.filter(user_id=request.user,closet)
    return render(request, 'contents/closet_filter.html',{'object_list':object_list})
"""

"""
def Itemlistview(request):
    object_list = Item.objects.filter(user_id = request.user)
    return render(request, 'contents/item_list.html',{'object_list':object_list})

def Itemlisting(request):
    item_list = Item.objects.filter(user_id = request.user)
    paginator = Paginator(item_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/paginator.html', {'page_object': page_object})

"""
