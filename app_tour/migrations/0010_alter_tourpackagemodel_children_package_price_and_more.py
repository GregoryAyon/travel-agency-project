# Generated by Django 4.2.2 on 2023-08-15 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tour', '0009_tourpackagemodel_children_package_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpackagemodel',
            name='Children_package_price',
            field=models.FloatField(default=50, help_text='Enter 50 percent children traveler', null=True),
        ),
        migrations.AlterField(
            model_name='tourpackagemodel',
            name='Infant_package_price',
            field=models.FloatField(default=90, help_text='Enter 90 percent infant traveler', null=True),
        ),
        migrations.CreateModel(
            name='TourPaymentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_card_name', models.CharField(max_length=125, null=True)),
                ('user_card_number', models.CharField(max_length=125, null=True)),
                ('user_cvc_number', models.CharField(max_length=125, null=True)),
                ('user_postal_code', models.CharField(max_length=125, null=True)),
                ('adults_fare', models.FloatField(null=True)),
                ('childrens_fare', models.FloatField(blank=True, null=True)),
                ('infants_fare', models.FloatField(blank=True, null=True)),
                ('sub_total_fare', models.FloatField(null=True)),
                ('total_fare', models.FloatField(null=True)),
                ('is_paid', models.BooleanField(default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_tour.tourordermodel')),
            ],
            options={
                'verbose_name': 'Tour Package Payment',
                'verbose_name_plural': 'Tour Package Payments',
                'ordering': ['-id'],
            },
        ),
    ]