# Generated by Django 4.2.1 on 2023-09-22 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_device_type_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image_url',
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/services/img/'),
        ),
    ]
