# Generated by Django 3.2.16 on 2022-12-30 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecasting', '0002_stats_stroke_lbl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='stroke_prob',
            field=models.CharField(max_length=50),
        ),
    ]
