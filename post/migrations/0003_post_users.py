# Generated by Django 4.1.7 on 2023-03-18 10:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_post_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='favorite_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]