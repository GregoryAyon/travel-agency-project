# Generated by Django 4.2.2 on 2023-08-15 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tour', '0010_alter_tourpackagemodel_children_package_price_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tourpackageimages',
            options={'ordering': ['-id'], 'verbose_name': 'Tour Package Image', 'verbose_name_plural': 'Tour Package Images'},
        ),
        migrations.AddField(
            model_name='tourpaymentsmodel',
            name='total_traveler',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]