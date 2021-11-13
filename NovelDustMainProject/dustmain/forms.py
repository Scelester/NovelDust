from django.forms import ModelForm
from .models import *

class Topbookform(ModelForm):
    class Meta:
        model = TopBooks
        fields = ['topname','topcover']

class BookItemsForm(ModelForm):
    class Meta:
        model = BookItems
        fields = ['topbook','name',
                    'cover','samename',
                    'samecover','volume_no']