# Generated by Django 3.1.2 on 2021-09-08 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0069_auto_20210908_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newfacultyload',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='counselling.faculty'),
        ),
    ]
