# Generated by Django 4.0.6 on 2022-12-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0006_user_post_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
