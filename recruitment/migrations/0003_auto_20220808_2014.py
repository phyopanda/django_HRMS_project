# Generated by Django 2.0 on 2022-08-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20220808_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentmodel',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]