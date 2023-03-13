# Generated by Django 4.0.6 on 2023-03-13 08:05

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0016_alter_user_post_image_alter_user_post_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='user_post',
            name='profileImg',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='profilePic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]