from django.shortcuts import render, redirect
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.core.paginator import Paginator
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# from rofiq.decorators import tolakhalaman_ini,ijinkan_pengguna,pilihan_login


from .models import *
from .forms import OrderForm, CustumerForm, RegisterForm
from .filters import OrderFilter
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
from django.contrib.auth.models import Group


@login_required(login_url='login') 
@ijinkan_pengguna(yang_diizinkan=['custumer'])
def accountSetting(request):
    datacustumer = request.user.custumer
    form = CustumerForm(instance = datacustumer)
    if request.method == 'POST':
        form = CustumerForm(request.POST, request.FILES, instance=datacustumer)
        if form.is_valid:
            form.save()
    context = {
        'menu': 'settings',
        'formcus': form
    }
    return render(request, 'data/account_setting.html', context)


@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['custumer'])
def userPage(request):
    order_custumer = request.user.custumer.order_set.all()
    total_orders = order_custumer.count()
    delivered = order_custumer.filter(status = 'Delivered').count()
    pending = order_custumer.filter(status = 'Pending').count()
    out_delivery = order_custumer.filter(status = 'Out for delivery').count()
    context = {
        'data_order_custumer':order_custumer,
        'data_total_orders': total_orders,
        'data_delivered' : delivered,
        'data_pending' : pending,
        'data_out' : out_delivery,
    }
    return render(request, 'user.html', context)

@tolakhalaman_ini
def loginPage (request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    formlogin = AuthenticationForm
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'Username Tidak ditemukan')
            return redirect('login')
        if not user_obj.is_active:
            messages.success(request, 'Data login masih belum di aktivasi, silakan cek email untuk aktivasi')
            return redirect('login')

        cocokan = authenticate(request, username=username, password=password )
        if cocokan is not None:
            login(request, cocokan)
            return redirect('home')
    context = {
    'judul': 'Halaman Login',
    'menu': 'login',
    'tampillogin' : formlogin
    }
    return render(request, 'login.html', context)

@tolakhalaman_ini
def registerPage (request):
    formregister = RegisterForm()
    if request.method == 'POST':
        formregister = RegisterForm(request.POST)
        if formregister.is_valid():
            nilaiusername = formregister.cleaned_data.get('username')
            messages.success(request, f'Username Anda adalah {nilaiusername}')
            group_custumer = formregister.save()
            grup = Group.objects.get(name='custumer')
            group_custumer.groups.add(grup)
            Custumer.objects.create(
                user=group_custumer,
                name=group_custumer.username)
            # pengguna = formregister.save()
            # pengguna.is_active = False
            # pengguna.save()
            return redirect('login')
    context = {
        'judul': 'Halaman Register',
        'menu': 'register',
        'tampilregister' : formregister
    }
    return render(request, 'register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@pilihan_login
def home(request):
    list_custumer = Custumer.objects.order_by('id')
    list_order = Order.objects.order_by('-id')
    total_orders = list_order.count()
    delivered = list_order.filter(status = 'Delivered').count()
    pending = list_order.filter(status = 'Pending').count()
    out_delivery = list_order.filter(status = 'Out for delivery').count()

    context = {
        'judul': 'Halaman Beranda',
        'menu': 'home',
        'custumer':list_custumer,
        'order':list_order,
        'data_total_orders': total_orders,
        'data_delivered' : delivered,
        'data_pending' : pending,
        'data_out' : out_delivery,
    }
    return render(request, 'data/home.html', context)   

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def products(request):
    list_product = Product.objects.all()
    context = {
        'judul': 'Halaman Products',
        'menu': 'products',
        'product': list_product,
    }
    return render(request, 'data/products.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
@login_required(login_url='login')
def custumer(request,pk):
    list_custumer = Custumer.objects.all()
    detailcustumer = Custumer.objects.get(id=pk)
    order_custumer = detailcustumer.order_set.order_by('-id')
    total_custumer = order_custumer.count()
    filter_order = OrderFilter(request.GET, queryset=order_custumer)
    order_custumer=filter_order.qs

    halaman_tampil = Paginator(order_custumer, 2)
    halaman_url = request.GET.get('halaman',1)
    halaman_order = halaman_tampil.get_page(halaman_url)

    if halaman_order.has_previous():
        url_previous = f'?halaman={halaman_order.previous_page_number()}'
    else:
        url_previous = ''
    if halaman_order.has_next():
        url_next = f'?halaman={halaman_order.next_page_number()}'
    else:
        url_next = ''
    
    context = {
        'judul': 'Halaman Konsumen',
        'menu': 'custumer',
        'custumer_list':list_custumer,
        'custumer': detailcustumer,
        # 'data_order_custumer':order_custumer,
        'halaman_order_custumer':halaman_order,
        'data_total_custumer': total_custumer,
        'filter_data_order': filter_order,
        'previous' : url_previous,
        'next' : url_next
    }
    return render(request, 'data/custumer.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
def createCustumer(request):
    formcustumer = CustumerForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = CustumerForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
    context = {
        'judul': 'Form Customer',
        'formcus' : formcustumer, 
    }
    return render(request, 'data/custumer_form.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
def updateCustumer(request,pk):
    custumer = Custumer.objects.get(id=pk)
    formcustumer = CustumerForm(instance=custumer)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formupdate = CustumerForm(request.POST, instance=custumer)
        if formupdate.is_valid:
            formupdate.save()
            return redirect('/')
    context = {
        'judul': 'update custumer',
        'formcus' : formcustumer, 
        # 'custumer': custumer,
    }
    return render(request, 'data/custumer_form.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
def deleteCustumer(request, pk):
    custumerhapus = Custumer.objects.get(id=pk)
    if request.method == 'POST':
        custumerhapus.delete()
        return redirect('/')
    context = {
        'judul': 'Hapus Data Customer',
        'datacustumerdelete' : custumerhapus, 
    }
    return render(request, 'data/delete_custumer.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
def createOrder(request):
    formorder = OrderForm()
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formsimpan = OrderForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
    context = {
        'judul': 'Form Order',
        'form' : formorder, 
    }
    return render(request, 'data/order_form.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    formorder = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Cetak POST:', request.POST)
        formedit = OrderForm(request.POST, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('/')
    context = {
        'judul': 'Edit Order',
        'form' : formorder, 
    }
    return render(request, 'data/order_form.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin'])
def deleteOrder(request, pk):
    orderhapus = Order.objects.get(id=pk)
    if request.method == 'POST':
        orderhapus.delete()
        return redirect('/')
    context = {
        'judul': 'Hapus Data Order',
        'dataorderdelete' : orderhapus, 
    }
    return render(request, 'data/delete_form.html', context)

# def home_page(request, name):
# # ---- #
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")
#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)
#     if match_object:
#         clean_name = match_object.group(0)
#     else:
#         clean_name = "Friend"

#     content = "Hello Rofiq, " + clean_name + "! It's " + formatted_now
#     return HttpResponse(content)
