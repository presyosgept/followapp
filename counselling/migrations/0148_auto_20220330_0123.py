# Generated by Django 3.1.2 on 2022-03-29 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0147_newdepartment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allsubject',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling.newdepartment'),
        ),
    ]
