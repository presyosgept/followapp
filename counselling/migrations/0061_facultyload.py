# Generated by Django 3.1.2 on 2021-09-08 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0060_delete_facultyload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultyload',
            fields=[
                ('offer_no', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('employeeid', models.CharField(max_length=220)),
            ],
        ),
    ]
