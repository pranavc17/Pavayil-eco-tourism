# Generated by Django 4.0.4 on 2022-06-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_resort'),
    ]

    operations = [
        migrations.CreateModel(
            name='idgen2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resort_id', models.IntegerField()),
            ],
            options={
                'db_table': 'idgen2',
            },
        ),
    ]