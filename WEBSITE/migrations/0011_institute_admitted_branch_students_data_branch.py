# Generated by Django 5.0.3 on 2024-04-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0010_students_data_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute_admitted',
            name='branch',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='students_data',
            name='branch',
            field=models.CharField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
