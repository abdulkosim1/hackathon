# Generated by Django 4.1.7 on 2023-03-18 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='users',
        ),
    ]