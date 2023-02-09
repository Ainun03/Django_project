# from django.forms import TextInput, Textarea, TypedChoiceField
# from django.db import models
# from django.contrib.admin import AdminSite

from django.contrib import admin
from .models import *

# Register your models here.
# class RofiqAdminSite(AdminSite):
#     site_header = "UMSRA Events Admin"
#     site_title = "UMSRA Events Admin Portal"
#     index_title = "Welcome to UMSRA Researcher Events Portal"

# rofiq_admin_site = RofiqAdminSite(name='rofiq_admin')

admin.site.register(Custumer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)