# Generated by Django 4.0.1 on 2022-01-21 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_category_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='undefined', max_length=255),
        ),
    ]
