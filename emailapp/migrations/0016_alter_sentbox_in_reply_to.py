# Generated by Django 4.2.13 on 2024-07-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0015_remove_mailbox_headers_alter_mailbox_in_reply_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentbox',
            name='in_reply_to',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
