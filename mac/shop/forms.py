# forms.py

from django import forms
from tinymce.widgets import TinyMCE
from .models import Product

class ProductAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Product
        fields = '__all__'
