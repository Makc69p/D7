from django_filters import FilterSet, ModelChoiceFilter
from .models import Product, Material


class ProductFilter(FilterSet):
    material = ModelChoiceFilter(
        field_name= 'productmaterial_material',
        queryset= Material.objects.all(),
        label='Material',
        conjoined=True,

    )



   class Meta:
       model = Product
       fields = {
           'productmaterial_material': ['exact'],
           'name': ['icontains'],
           'quantity': ['gt'],
           'price': [
               'lt',
               'gt',
           ],
       }