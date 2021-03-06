# Generated by Django 3.0.6 on 2020-05-20 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20200517_0218'),
        ('sms', '0004_remove_message_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, to='contacts.Contact'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='message_info',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='sms.SmsInfo'),
        ),
        migrations.AlterField(
            model_name='message',
            name='number',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
