# Generated by Django 5.1.3 on 2024-11-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_profileuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profileuser',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
