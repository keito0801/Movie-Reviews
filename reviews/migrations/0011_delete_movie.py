# Generated by Django 3.2.3 on 2021-06-09 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_review_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
