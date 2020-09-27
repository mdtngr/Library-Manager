from django.forms import ModelForm
from items.models import ItemDetails
from items import models



class AddItemForm(ModelForm):
    class Meta():
        model = models.ItemDetails
        fields = ['item_name', 'hsn_code', 'publisher', 'shelf','item_quantity', 'author', 'item_category', 'item_image']

