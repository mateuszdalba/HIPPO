# Generated by Django 3.2.16 on 2023-01-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_fasting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fasting',
            name='date_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fasting',
            name='date_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
