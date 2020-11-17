from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render
from items.models import (ItemDetails)
# from items.forms import (AddItemForm, QueryItemForm)
from items.forms import (AddItemForm)

from django.db.models import Q

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
    # context['form'] = QueryItemForm()
       
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



# Item Filter View
@csrf_protect
def filter_item_view(request):
    Query = str(request.POST['data'])
    
    queries = list(set(Query.split(" ")))
    

    all_items = ItemDetails.objects.all
    filtered_items = all_items

    # for q in queries:
    #     all_items = ItemDetails.objects.filter(Q(item_name__icontains = q )).distinct()

    #     print(all_items)

    #     for val in all_items:
    #         # filtered_items.append(val)
    #         print(all_items)

    # filtered_items = list(set(filtered_items))
    
    data = { 'a': filtered_items }
    return JsonResponse(data)
