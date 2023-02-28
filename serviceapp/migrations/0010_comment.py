# Generated by Django 4.0.6 on 2022-12-26 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0009_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('post_id', models.CharField(max_length=500)),
                ('commenter', models.CharField(max_length=100)),
                ('created_At', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]