# Generated by Django 5.0.2 on 2024-02-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': '계열',
                'verbose_name_plural': '계열',
            },
        ),
    ]
