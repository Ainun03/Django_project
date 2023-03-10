import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class OrderFilter(django_filters.FilterSet):
    tglmulai = DateFilter(field_name="date_created", lookup_expr='gte')
    tglakhir = DateFilter(field_name="date_created", lookup_expr='lte')
    note = CharFilter(field_name="note", lookup_expr='icontains' )
    class Meta:
        model = Order
        fields ='__all__'
        exclude = ['custumer','date_created']
        # widgets = {
        #     # 'custumer': forms.Select(attrs={'class': 'form-control'}),
        #     'product': forms.Select(attrs={'class': 'form-control'}),
        #     'status': forms.Select(attrs={'class': 'form-control'})
        # }
        # labels = {
        #     # 'custumer': 'Konsumen',
        #     'product': 'Produk',
        #     'status': 'Status Order',
        # }
