# Generated by Django 4.0.4 on 2022-06-28 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_rename_id_proof_traveller_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='homestaybooking',
            fields=[
                ('homestaybooking_id', models.CharField(max_length=90, primary_key=True, serialize=False)),
                ('booking_date', models.CharField(max_length=90)),
                ('no_of_days', models.CharField(max_length=30)),
                ('no_of_person', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('homestay_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.homestay')),
                ('traveller_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.traveller')),
            ],
            options={
                'db_table': 'homestaybooking',
            },
        ),
    ]
