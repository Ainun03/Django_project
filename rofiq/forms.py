from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order, Custumer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields= '__all__'
        widgets = {
            'custumer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }
        labels = {
            'custumer': 'Konsumen',
            'product': 'Produk',
            'status': 'Status Order',
        }
class CustumerForm(ModelForm):
    class Meta:
        model = Custumer
        fields= '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Nama',
            'phone': 'No Handphone',
            'email': 'Email',
        }
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields= ['username','email','password1','password2']