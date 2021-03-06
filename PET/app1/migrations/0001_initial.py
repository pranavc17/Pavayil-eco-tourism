# Generated by Django 4.0.4 on 2022-06-14 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity',
            fields=[
                ('activity_id', models.CharField(max_length=90, primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=90)),
                ('photo', models.ImageField(upload_to='')),
                ('rate', models.IntegerField()),
                ('status', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='idgen1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.IntegerField()),
            ],
            options={
                'db_table': 'idgen1',
            },
        ),
    ]
