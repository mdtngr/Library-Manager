from django.shortcuts import render, redirect
from transactions.models import TransactionDetails
from transactions.forms import (AddTransactionForm)

# Create your views here.


def all_txn_view(request):
    # print(request.headers)
    context={}
    context['all_txn'] = TransactionDetails.objects.all()
    
    return render(request, 'transactions/txn.html', context)


def  add_txn_view(request):
    context =   {}
      

    if request.method == 'POST':
        add_txn_form    =   AddTransactionForm(request.POST)
        context['add_txn_form'] = add_txn_form
        
        if add_txn_form.is_valid():
            # process form data
            obj = TransactionDetails() #gets new object
            obj.txn_type = add_txn_form.cleaned_data['txn_type']
            obj.user = add_txn_form.cleaned_data['user']
            obj.amount = add_txn_form.cleaned_data['amount']            
            obj.item = add_txn_form.cleaned_data['item']
            print(obj)
            
            # finally save the object in db
            obj.save()

            return redirect('txn')
        
        else:
            add_txn_form = AddTransactionForm()
            context['add_txn_form'] = add_txn_form
            return render(request, 'add_txn.html',context)
    
    else:
        add_txn_form = AddTransactionForm()
        context['add_txn_form'] = add_txn_form
        return render(request, 'transactions/add_txn.html', context)
            
    return redirect('txn')