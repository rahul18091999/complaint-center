# Generated by Django 2.2.12 on 2020-05-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0003_auto_20200524_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='Department_name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
