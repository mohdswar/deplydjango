# Generated by Django 5.1.7 on 2025-03-24 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.ManyToManyField(to='my_app.role'),
        ),
    ]
