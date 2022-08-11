# Generated by Django 4.0.6 on 2022-08-04 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_author_options_rename_first_name_author_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'author']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, null=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', '保存'), ('o', '借出'), ('a', '可借'), ('r', '预约')], default='m', help_text='Book availability', max_length=1),
        ),
    ]
