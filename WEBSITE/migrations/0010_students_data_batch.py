# Generated by Django 5.0.3 on 2024-04-09 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0009_students_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='students_data',
            name='batch',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
    ]
