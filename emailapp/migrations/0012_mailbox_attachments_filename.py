# Generated by Django 4.2.13 on 2024-07-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0011_mailbox_attachments_remove_mailbox_attachements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailbox_attachments',
            name='filename',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]