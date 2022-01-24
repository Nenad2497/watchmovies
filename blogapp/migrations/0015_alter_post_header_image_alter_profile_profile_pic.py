# Generated by Django 4.0.1 on 2022-01-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_alter_post_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]