# Generated by Django 4.2.1 on 2023-06-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('date_of_birth', models.DateField(auto_now=True)),
                ('email', models.CharField(max_length=32)),
                ('phone_number', models.CharField(max_length=32)),
            ],
        ),
    ]
