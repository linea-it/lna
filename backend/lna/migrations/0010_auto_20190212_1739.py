# Generated by Django 2.1.5 on 2019-02-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lna', '0009_exposure_exposure_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exposure',
            name='band',
            field=models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name='Band'),
        ),
    ]
