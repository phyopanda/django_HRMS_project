# Generated by Django 2.2.13 on 2022-07-23 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0021_auto_20220724_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='emp_id',
            field=models.CharField(default='emp896', max_length=70),
        ),
    ]
