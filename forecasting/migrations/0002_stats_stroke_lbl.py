# Generated by Django 3.2.16 on 2022-12-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='stroke_lbl',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]