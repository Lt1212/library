# Generated by Django 4.0.6 on 2022-08-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_author_summary_alter_author_image_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='sex',
            field=models.CharField(blank=True, choices=[('F', '女'), ('M', '男'), ('O', '其他')], default='m', help_text='性别', max_length=1),
        ),
    ]
