# Generated by Django 4.0.6 on 2022-08-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(default='media/author/default.jpg', upload_to='author'),
        ),
    ]
