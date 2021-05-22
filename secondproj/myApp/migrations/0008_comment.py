# Generated by Django 3.2.2 on 2021-05-22 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_auto_20210512_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.TextField(max_length=20)),
                ('content', models.TextField(max_length=100)),
                ('blog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.blog')),
            ],
        ),
    ]
