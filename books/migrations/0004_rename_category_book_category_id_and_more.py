# Generated by Django 5.1.6 on 2025-03-03 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_rename_descreption_book_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='user',
            new_name='user_id',
        ),
    ]
