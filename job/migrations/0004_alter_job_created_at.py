# Generated by Django 4.0.6 on 2022-08-06 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_job_created_at_alter_job_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 6, 5, 40, 23, 530584)),
        ),
    ]
