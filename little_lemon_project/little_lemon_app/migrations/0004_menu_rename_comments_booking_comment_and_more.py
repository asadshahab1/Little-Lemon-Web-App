# Generated by Django 5.0.4 on 2024-04-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('little_lemon_app', '0003_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='comments',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='guest_count',
            new_name='guest_number',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='reservation_time',
        ),
    ]
