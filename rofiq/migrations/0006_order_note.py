# Generated by Django 4.1.3 on 2022-12-04 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rofiq', '0005_alter_custumer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
