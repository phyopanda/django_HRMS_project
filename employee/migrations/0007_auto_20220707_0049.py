# Generated by Django 2.0 on 2022-07-06 18:19

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0002_contractmodel_job_id'),
        ('employee', '0006_auto_20220707_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemodel',
            name='contract_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contract.ContractModel'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2022, 7, 6, 18, 19, 54, 420723, tzinfo=utc), verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='employeemodel',
            name='emp_id',
            field=models.CharField(default='emp834', max_length=70),
        ),
    ]