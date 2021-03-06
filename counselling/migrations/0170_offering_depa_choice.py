# Generated by Django 3.1.2 on 2022-04-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counselling', '0169_auto_20220503_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='offering',
            name='depa_choice',
            field=models.CharField(choices=[['Department of Language and Literature', 'Department of Language and Literature'], ['Department of Social Sciences and Philosophy', 'Department of Social Sciences and Philosophy'], ['Department of Mathematics and Sciences', 'Department of Mathematics and Sciences'], ['Department of Journalism and Communication', 'Department of Journalism and Communication'], ['Department of Psychology and Library Information Science', 'Department of Psychology and Library Information Science'], ['Department of Accountancy and Finance', 'Department of Accountancy and Finance'], ['Department of Business and Entrepreneurship', 'Department of Business and Entrepreneurship'], ['Department of Marketing and Human Resource Management', 'Department of Marketing and Human Resource Management'], ['Department of Computer Science and Information Technology', 'Department of Computer Science and Information Technology'], ['Student Development and Placement Center', 'Student Development and Placement Center'], ['Center for Religious Education', 'Center for Religious Education'], ['Safety and Security Department', 'Safety and Security Department'], ['Department of Education', 'Department of Education']], default='---', max_length=220),
        ),
    ]
