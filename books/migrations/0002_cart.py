# Generated by Django 4.2.10 on 2024-03-08 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
            ],
        ),
    ]
