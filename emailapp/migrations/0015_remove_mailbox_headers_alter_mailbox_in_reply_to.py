# Generated by Django 4.2.13 on 2024-07-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0014_mailbox_headers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailbox',
            name='headers',
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='in_reply_to',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
