from django.forms import ModelForm
from .models import Brand, Product

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ['brand_name']

# class ProductForm(ModelForm):
#     class Meta:
#         model = Product
#         fields = ['product_name', 'descrpt', 'fk_category', 'price', 'quantity']