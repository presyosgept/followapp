# Generated by Django 3.1.2 on 2022-02-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0146_auto_20220223_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselor',
            name='school_choice',
            field=models.CharField(choices=[('School of Computer Studies', 'School of Computer Studies'), ('School of Education', 'School of Education'), ('School of Engineering', 'School of Engineering'), ('School of Arts and Sciences', 'School of Arts and Sciences'), ('School of Business and Management', 'School of Business and Management'), ('Center for Religious Education', 'Center for Religious Education'), ('Student Development and Placement Center', 'Student Development and Placement Center')], default='School of Computer Studies', max_length=220),
        ),
        migrations.AlterField(
            model_name='counselor',
            name='program_designation',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]