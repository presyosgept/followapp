# Generated by Django 3.1.2 on 2021-07-03 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('employeeid', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=220)),
                ('lastname', models.CharField(max_length=220)),
                ('program_designation', models.CharField(choices=[('BSIT', 'BSIT'), ('BSPT', 'BSPT'), ('BSMT', 'BSMT')], max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Facultyload',
            fields=[
                ('offer_no', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('employeeid', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('studnumber', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=220)),
                ('lastname', models.CharField(max_length=220)),
                ('email', models.CharField(max_length=220)),
                ('role', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Studentsload',
            fields=[
                ('id', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('offer_no', models.CharField(max_length=220)),
                ('studnumber', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectOffered',
            fields=[
                ('offer_no', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('subject_no', models.CharField(max_length=220)),
                ('subject_title', models.CharField(max_length=220)),
                ('day', models.CharField(max_length=220)),
                ('time', models.CharField(max_length=220)),
                ('units', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Teachersload',
            fields=[
                ('employeeid', models.CharField(max_length=220, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=220)),
                ('lastname', models.CharField(max_length=220)),
                ('external_email', models.CharField(max_length=220)),
                ('role', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='TeachersReferral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studnumber', models.CharField(max_length=220)),
                ('firstname', models.CharField(max_length=220)),
                ('lastname', models.CharField(max_length=220)),
                ('degree_program', models.CharField(max_length=220)),
                ('subject_referred', models.CharField(max_length=220)),
                ('reasons', models.CharField(max_length=10000)),
                ('counselor', models.CharField(max_length=220)),
                ('employeeid', models.CharField(blank=True, max_length=220, null=True)),
            ],
        ),
    ]
