# Generated by Django 3.2.2 on 2021-05-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albamon_app', '0012_auto_20210522_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applier',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='information',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='pay',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='work',
            field=models.TextField(max_length=100),
        ),
    ]