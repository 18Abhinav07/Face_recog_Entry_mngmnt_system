# Generated by Django 5.0.3 on 2024-04-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0011_institute_admitted_branch_students_data_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institute_admitted',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='non_institute_admitted',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='students_data',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
