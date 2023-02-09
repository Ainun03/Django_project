from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Custumer(models.Model):
       user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
       name = models.CharField(max_length=200, blank=True, null=True)
       phone = models.CharField(max_length=200, blank=True, null=True)
       email = models.CharField(max_length=200, blank=True, null=True)
       date_created= models.DateTimeField(auto_now_add=True, null=True)
       profile_pic = models.ImageField(null=True, blank=True ,  upload_to='gambar')
       def __str__(self):
              return self.name
       # def __str__(self):
       #        return '%s, %s' % (self.name, self.phone)
       def save(self, *args, **kwargs):
              super(Custumer, self).save(*args, **kwargs)
              img = Image.open(self.profile_pic.path)
             
              if img.height > 300 or img.width > 300:
                     output_size = (300,300)
                     img.thumbnail(output_size)
                     img.save(self.profile_pic.path)
       class Meta:
              verbose_name_plural = "Konsumen"

class Tag(models.Model):
       name = models.CharField(max_length=200, blank=True, null=True)
       def __str__(self):
              return self.name


class Product(models.Model):
       CATEGORY=(
              ('Indoor', 'Indoor'),
              ('Out Door' , 'Out Door'),
       )
       class Meta:
              verbose_name_plural = "Produk"

       name = models.CharField(max_length=200, blank=True, null=True)
       price = models.IntegerField(blank=True, null=True)
       category = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
       description = models.CharField(max_length=200, blank=True, null=True)
       tag = models.ManyToManyField(Tag)
       date_created= models.DateTimeField(auto_now_add=True, null=True)
       gambar= models.ImageField(upload_to='gambar/produk', blank=True, null=True, verbose_name="Gambar (1200 x 700)")
       def __str__(self):
              return self.name

class Order(models.Model):
       STATUS=(
              ('Pending', 'Pending'),
              ('Out for delivery' , 'Out for delivery'),
              ('Delivered', 'Delivered'),
       )
       
       custumer = models.ForeignKey(Custumer, null=True, on_delete=models.SET_NULL)
       product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
       date_created = models.DateTimeField(auto_now_add=True, null=True)
       status = models.CharField(max_length=200, null=True, choices=STATUS)
       note = models.CharField(max_length=200, blank=True, null=True)
       def __str__(self):
              # return '%s, %s' % (self.status, self.custumer)
              return self.product.name
              

