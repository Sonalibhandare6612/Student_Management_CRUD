# Generated by Django 4.1.1 on 2023-05-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('regNumber', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
