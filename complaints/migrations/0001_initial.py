# Generated by Django 2.2.12 on 2020-05-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(max_length=20)),
                ('HOD_username', models.CharField(max_length=50)),
                ('HOD_name', models.CharField(max_length=50)),
                ('HOD_email', models.EmailField(max_length=254)),
                ('HOD_phno', models.IntegerField()),
            ],
        ),
    ]
