# Generated by Django 3.1.2 on 2021-08-30 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0042_faculty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='employee_id',
            new_name='employeeid',
        ),
    ]
