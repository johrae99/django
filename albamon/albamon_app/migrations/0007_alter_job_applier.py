# Generated by Django 3.2.2 on 2021-05-22 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albamon_app', '0006_alter_job_applier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applier',
            field=models.IntegerField(default=0),
        ),
    ]
