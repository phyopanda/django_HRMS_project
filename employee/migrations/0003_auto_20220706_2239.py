# Generated by Django 2.0 on 2022-07-06 16:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220706_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 7, 6, 16, 9, 21, 619439, tzinfo=utc), verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='emp_id',
            field=models.CharField(default='emp751', max_length=70),
        ),
    ]