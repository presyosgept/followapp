# Generated by Django 3.1.2 on 2021-10-13 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0089_auto_20211013_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsload',
            name='studnumber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counselling.allstudents'),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
