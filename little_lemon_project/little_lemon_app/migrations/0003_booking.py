# Generated by Django 5.0.4 on 2024-04-05 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('little_lemon_app', '0002_rename_drink_drinks_drink_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('guest_count', models.IntegerField()),
                ('reservation_time', models.DateField(auto_now=True)),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]
