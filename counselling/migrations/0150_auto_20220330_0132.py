# Generated by Django 3.1.2 on 2022-03-29 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0149_auto_20220330_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allsubject',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling.department'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling.department'),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_code', models.CharField(max_length=225, primary_key=True, serialize=False)),
                ('subject_title', models.CharField(max_length=220)),
                ('units', models.CharField(max_length=220)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='counselling.newdepartment')),
            ],
        ),
    ]