# Generated by Django 3.1.2 on 2021-08-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0032_delete_studentschedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolOffices',
            fields=[
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('school_code', models.CharField(max_length=220)),
                ('school_office_name', models.CharField(max_length=220)),
            ],
        ),
    ]