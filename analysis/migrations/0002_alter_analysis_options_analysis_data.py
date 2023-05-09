# Generated by Django 4.1.3 on 2022-12-01 22:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'verbose_name_plural': 'analyses'},
        ),
        migrations.AddField(
            model_name='analysis',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]