from django import forms
from .models import Product, DeleteProduct

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']
        
        

class Delete_Product_Form(forms.ModelForm):
    class Meta:
        model = DeleteProduct
        fields = ['delete']
