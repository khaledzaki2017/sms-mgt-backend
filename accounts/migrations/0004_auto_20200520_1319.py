# Generated by Django 3.0.6 on 2020-05-20 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformation',
            name='time_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinformation',
            name='time_last_edited',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
