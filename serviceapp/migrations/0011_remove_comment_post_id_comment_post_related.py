# Generated by Django 4.0.6 on 2022-12-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0010_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_related',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceapp.user_post'),
        ),
    ]
