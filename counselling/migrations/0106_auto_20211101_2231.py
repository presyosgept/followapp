# Generated by Django 3.1.2 on 2021-11-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0105_auto_20211101_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='schedTime',
            new_name='schedEndTime',
        ),
        migrations.AddField(
            model_name='notification',
            name='schedStartTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
