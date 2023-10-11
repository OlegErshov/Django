# Generated by Django 4.2.1 on 2023-09-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_stuff_client_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='image',
            field=models.FileField(blank=True, upload_to='static/services/img/'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='mark',
            field=models.DecimalField(decimal_places=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='text',
            field=models.TextField(max_length=350),
        ),
    ]