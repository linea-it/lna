# Generated by Django 2.1.5 on 2019-02-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lna', '0008_auto_20190211_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='exposure',
            name='exposure_time',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Exposure Time'),
        ),
    ]