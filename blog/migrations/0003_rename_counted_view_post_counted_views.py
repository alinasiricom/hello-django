# Generated by Django 4.2.14 on 2024-07-25 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_counted_view_post_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='counted_view',
            new_name='counted_views',
        ),
    ]