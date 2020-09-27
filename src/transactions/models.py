from django.db import models
from users.models import UserData
from items.models import ItemDetails
from datetime import datetime    



# Create your models here.

class TransactionDetails(models.Model):
    txn_id             = models.IntegerField(null=False, primary_key=True)
    txn_type           = models.BooleanField(null=False, default=False)
    txn_date           = models.DateTimeField(auto_now_add= True)
    amount             = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0.0)
    user               = models.ForeignKey(UserData, on_delete=models.CASCADE, blank=False, null=False)
    item               = models.ForeignKey(ItemDetails, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
    	return self.user




