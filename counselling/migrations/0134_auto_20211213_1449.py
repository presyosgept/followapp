# Generated by Django 3.1.2 on 2021-12-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0133_auto_20211213_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='contact_number',
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='degree_program',
            field=models.CharField(max_length=220),
        ),
    ]
