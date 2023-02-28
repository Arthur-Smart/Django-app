# Generated by Django 4.0.6 on 2022-12-22 13:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField()),
                ('service', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('biography', models.TextField(blank=True)),
                ('profilePic', models.ImageField(default='default.jpg', upload_to='profile_images')),
                ('created_At', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
