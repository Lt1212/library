# Generated by Django 4.0.6 on 2022-08-06 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='media/book/default.jpg', upload_to='book'),
        ),
    ]
