# Generated by Django 4.2.13 on 2024-07-17 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0025_mailboxbundle'),
    ]

    operations = [
        migrations.RenameField(
            model_name='draftbox',
            old_name='aasignedTo',
            new_name='assignedTo',
        ),
        migrations.RenameField(
            model_name='mailbox',
            old_name='aasignedTo',
            new_name='assignedTo',
        ),
        migrations.RenameField(
            model_name='sentbox',
            old_name='aasignedTo',
            new_name='assignedTo',
        ),
    ]