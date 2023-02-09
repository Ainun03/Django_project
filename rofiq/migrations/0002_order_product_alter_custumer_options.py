# Generated by Django 4.1.3 on 2022-11-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rofiq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.AlterModelOptions(
            name='custumer',
            options={'verbose_name_plural': 'Consuments'},
        ),
    ]
