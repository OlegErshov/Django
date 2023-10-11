# Generated by Django 4.2.1 on 2023-10-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_news_resource'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='full_text',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='news',
            name='resource',
            field=models.CharField(default='', max_length=300),
        ),
    ]