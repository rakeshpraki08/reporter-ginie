# Generated by Django 3.2.16 on 2022-11-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_app', '0002_reports_task_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
