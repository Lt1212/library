# Generated by Django 4.0.6 on 2022-08-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_author_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='sex',
            field=models.CharField(blank=True, choices=[('F', '女'), ('M', '男'), ('O', '其他')], default='M', help_text='性别', max_length=1),
        ),
    ]
