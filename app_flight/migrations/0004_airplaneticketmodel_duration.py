# Generated by Django 4.2.2 on 2023-07-05 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_flight', '0003_alter_airplaneticketmodel_adult_tax_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplaneticketmodel',
            name='duration',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
