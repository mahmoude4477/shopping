# Generated by Django 4.2.10 on 2024-03-06 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='userId',
            field=models.IntegerField(default=0),
        ),
    ]
