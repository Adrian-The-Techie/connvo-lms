# Generated by Django 3.2.16 on 2024-08-28 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20240827_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='thumbnail',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.CharField(max_length=255),
        ),
    ]
