# Generated by Django 4.2.13 on 2024-07-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0012_mailbox_attachments_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='sentBox_attachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='sendAttachments/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('filename', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='sentbox',
            name='attachements',
        ),
        migrations.AddField(
            model_name='sentbox',
            name='attachements',
            field=models.ManyToManyField(blank=True, to='emailapp.sentbox_attachments'),
        ),
    ]