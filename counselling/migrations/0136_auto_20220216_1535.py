# Generated by Django 3.1.2 on 2022-02-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0135_auto_20211213_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='is_read',
            new_name='is_read_counselor',
        ),
        migrations.AddField(
            model_name='notification',
            name='is_read_student',
            field=models.BooleanField(default=False),
        ),
    ]