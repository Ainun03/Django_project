# Generated by Django 4.1.3 on 2022-12-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rofiq', '0008_custumer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custumer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='gambar'),
        ),
    ]