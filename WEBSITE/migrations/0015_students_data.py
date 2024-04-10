# Generated by Django 5.0.3 on 2024-04-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0014_delete_students_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='STUDENTS_DATA',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('room_no', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('batch', models.CharField(max_length=15)),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
    ]