# Generated by Django 4.2.2 on 2023-08-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tour', '0011_alter_tourpackageimages_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpackagemodel',
            name='package_cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='tour_package_cover_images'),
        ),
    ]
