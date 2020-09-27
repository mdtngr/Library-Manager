from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from items.models import (ItemDetails)
from items.forms import (AddItemForm,)

import json

# Create your views here.

# def all_item_admin_view(request):
#     context = {}
#     context['all_items'] = ItemDetails.objects.all()

#     return render(request, 'items/all_items.html', context)


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
            # process form data
            # obj = ItemDetails() #gets new object
            # obj.item_name = form.cleaned_data['item_name']
            # obj.hsn_code = form.cleaned_data['hsn_code']
            # obj.publisher = form.cleaned_data['publisher']
            # obj.shelf = form.cleaned_data['shelf']
            # obj.item_quantity = form.cleaned_data['item_quantity']
            # obj.author = form.cleaned_data['author']
            
            # print(obj)

            # finally save the object in db
            # obj.save()
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
    
def category_view(request):
    if not request.is_ajax():
        raise Http404
  
    # data_dict = getmydata()
    # return HttpResponse(json.dum
    # ps(data_dict))

    obj = {"a": 1, "b": 2}
    return render_to_response("template.html", {"obj_as_json": json.dumps(obj)})