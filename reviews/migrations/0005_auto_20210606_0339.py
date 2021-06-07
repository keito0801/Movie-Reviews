# Generated by Django 3.2.3 on 2021-06-06 07:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20210531_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='reviews.movie'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]