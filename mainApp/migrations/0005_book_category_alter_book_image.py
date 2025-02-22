# Generated by Django 5.0.3 on 2024-04-04 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0002_category_delete_book'),
        ('mainApp', '0004_alter_book_author_alter_book_image_alter_book_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categorie.category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books/images'),
        ),
    ]
