# Generated by Django 3.0.6 on 2020-05-04 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField(default=False, editable=False)),
                ('message_text', models.CharField(editable=False, max_length=255)),
                ('africastalking_response', models.CharField(editable=False, max_length=255)),
                ('time_sent', models.DateTimeField(editable=False)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['time_last_edited'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.CharField(editable=False, max_length=255)),
                ('status_code', models.CharField(editable=False, max_length=255)),
                ('number', models.CharField(editable=False, max_length=255)),
                ('cost', models.CharField(editable=False, max_length=255)),
                ('status', models.CharField(editable=False, max_length=255)),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('time_last_edited', models.DateTimeField(auto_now_add=True)),
                ('message_info', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sms.MessageInfo')),
            ],
            options={
                'order_with_respect_to': 'message_info',
            },
        ),
    ]
