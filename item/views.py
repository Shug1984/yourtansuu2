import datetime
import json
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count

from .models import Item, Closet, SEASON_CHOICES, OCCASION_CHOICES
from .forms import ItemForm, ClosetForm, SearchForm


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
    search_form = SearchForm(request.GET or None)
    if search_form.is_valid():
        input_form = request.GET.get('input_form')
        sort_form = request.GET.get('sort_form')
        if input_form:
            item_list = item_list.filter(item_name__icontains=input_form)
    
        if sort_form:
            item_list = item_list.order_by(sort_form)
        
    closet_list = [{ 'id':None, 'closet_name':'なし' }]+[{'id': obj.id, 'closet_name': obj.closet_name} for obj in Closet.objects.filter(user=request.user)]
    if request.GET.get('closet'):
        closet = request.GET['closet']
        item_list = item_list.filter(closet=closet)

    object_list = Closet.objects.filter(user_id = request.user)

    today = datetime.date.today()
    
    """import pdb;pdb.set_trace()"""
    paginator = Paginator(item_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/item_list.html', {
        'page_object': page_object, 'closet_list':closet_list,'today':today,'paginator':paginator,
        'search_form':search_form,'object_list':object_list
        })


@login_required
def ClosetChangeView(request):
    post_data = json.loads(request.body.decode("utf-8"))
    item_id = post_data.get('item_id')
    closet_id = post_data.get('closet_id')
    item = Item.objects.get(pk = item_id)
    item.closet_id = closet_id
    item.save()
    return JsonResponse({})
    

@login_required
def Itemdetailview(request, pk):
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


@login_required
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


@login_required
def ClosetCreateCompleteView(request):
    return render(request, 'contents/closet_create_complete.html')


@login_required
def ClosetListView(request):
    object_list = Closet.objects.filter(user_id = request.user)
    
    paginator = Paginator(object_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/closet_list.html', {'page_object': page_object})


@login_required
def ClosetUpdateView(request,pk):
    object_item = Closet.objects.get(user_id = request.user, pk=pk)
    if request.method == 'POST':
       form = ClosetForm(request.POST, instance=object_item)
       if form.is_valid():
           form.save()
           return redirect('closet_update_complete')
    else:
        form = ClosetForm(instance = object_item)
    return render(request, 'contents/closet_update.html',{'form':form, 'object_item':object_item})


@login_required
def ClosetUpdateCompleteView(request):
    return render(request, 'contents/closet_update_complete.html')


def ClosetDeleteView(request,pk):
    object_item = Closet.objects.get(user_id = request.user, pk=pk)
    if request.method == "POST":
        if request.POST.get('button','') == 'confirm':
            object_item.delete()
            return redirect('closet_delete_complete')
    
    else:
        return render(request, 'contents/closet_delete.html',{'object_item':object_item})


def ClosetDeleteCompleteView(request):
    return render(request, 'contents/closet_delete_complete.html')

   
@login_required
def SeasonGateView(request):
    return render(request, 'contents/season_gate.html')


@login_required
def SeasonListHomeView(request,season):
    object_list = Item.objects.filter(user_id=request.user, season=season)
    for item in SEASON_CHOICES:
        if season == item[0]:
            kisetsu = item[1]

    paginator = Paginator(object_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/season_list.html', {'page_object': page_object,'kisetsu':kisetsu})


@login_required
def OccasionGateView(request):
    return render(request, 'contents/occasion_gate.html')


@login_required
def OccasionListHomeView(request, occasion):
    object_list = Item.objects.filter(user_id=request.user, occasion=occasion)
    for item in OCCASION_CHOICES:
        if occasion == item[0]:
            kikai = item[1]
    
    paginator = Paginator(object_list, 10)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'contents/occasion_list.html', {'page_object': page_object, 'kikai':kikai})


def TestView(request):
    if request.method == "POST":
        target = request.POST.get('sorting_system')
        print(target)
        object_list = Item.objects.filter(user_id=request.user).order_by(target).reverse()
        print(object_list)
        return render(request, 'contents/testview2.html',{'object_list':object_list})
    
    else:
        return render(request, 'contents/testview.html')

    if request.method == "POST":
        query = request.POST.get('search_engine')
        print(query)
        object_list = Item.objects.filter(user_id=request.user,item_name__icontains=query)
        print(object_list)
        return render(request, 'contents/testview3.html', {'object_list':object_list})
    
    return render(request,'contents/testview.html')
