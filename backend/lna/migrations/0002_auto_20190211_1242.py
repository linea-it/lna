# Generated by Django 2.1.5 on 2019-02-11 12:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exposure',
            name='band',
            field=models.CharField(blank=True, default=None, max_length=5, null=True, verbose_name='Band'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='date_obs',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date Observation'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='dec',
            field=models.CharField(blank=True, default=None, max_length=12, null=True, verbose_name='Dec'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='file_type',
            field=models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='File Type'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='instrument',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Instrument'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='observer',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Observer'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='ra',
            field=models.CharField(blank=True, default=None, max_length=12, null=True, verbose_name='RA'),
        ),
        migrations.AddField(
            model_name='exposure',
            name='telescope',
            field=models.CharField(blank=True, default=None, max_length=256, null=True, verbose_name='Telescope'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='dec_deg',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Dec (deg)'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='file_path',
            field=models.FilePathField(blank=True, default=None, null=True, verbose_name='File Path'),
        ),
        migrations.AlterField(
            model_name='exposure',
            name='filename',
            field=models.CharField(default=django.utils.timezone.now, help_text='Filename', max_length=256, verbose_name='Filename'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exposure',
            name='ra_deg',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='RA (deg)'),
        ),
    ]
