# Generated by Django 4.1.3 on 2022-12-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_rename_data_analysis_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysis',
            name='image',
            field=models.ImageField(upload_to='analysis/images/'),
        ),
    ]