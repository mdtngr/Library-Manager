from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from items.models import (ItemDetails)
from items.forms import (AddItemForm,)

import json

# Create your views here.

def all_item_admin_view(request):
    context = {}
    context['all_items'] = ItemDetails.objects.all()

    return render(request, 'items/all_items_admin.html', context)


def get_all_categories():
    return  list({'Fiction','Thriller','Biography'})

def all_item_view(request):
    context = {}
    context['all_items'] = ItemDetails.objects.all()
    context['categories'] = get_all_categories()
    
    return render(request, 'items/all_items.html', context)


def  add_item_view(request):
    context =   {}

    if request.method == 'POST':
        form    =   AddItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/items/')

        else:
            context['add_item_form'] = form
    else: #GET
        pass
        # form = ItemRegistrationForm()
        # context['add_item_form'] = form
    return render(request, 'items/add_item.html',{})

def item_detail_view(request, book_id ):
    book_detail = ItemDetails.objects.get(hsn_code=book_id)
    return render(request , 'items/index.html',{'items':book_detail})