# Generated by Django 3.1.2 on 2022-04-05 14:09

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0156_auto_20220404_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersreferral',
            name='behavior_problem',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=220, null=True),
        ),
    ]