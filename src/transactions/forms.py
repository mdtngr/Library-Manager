from django.forms import ModelForm
from transactions.models import TransactionDetails
from transactions import models



class AddTransactionForm(ModelForm):
    class Meta():
        model = models.TransactionDetails
        fields = ['txn_type', 'amount', 'user', 'item']

