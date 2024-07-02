# Generated by Django 4.2.13 on 2024-07-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailapp', '0010_alter_mailbox_attachements'),
    ]

    operations = [
        migrations.CreateModel(
            name='mailBox_attachments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='emailAttachments/')),
                ('description', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='mailbox',
            name='attachements',
        ),
        migrations.AddField(
            model_name='mailbox',
            name='attachements',
            field=models.ManyToManyField(blank=True, to='emailapp.mailbox_attachments'),
        ),
    ]
