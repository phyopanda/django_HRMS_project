# Generated by Django 2.0 on 2022-08-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_contractmodel_job_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='salary',
            field=models.CharField(default='00,000.00', max_length=16),
        ),
    ]
