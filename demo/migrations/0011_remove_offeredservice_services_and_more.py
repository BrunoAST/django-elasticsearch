# Generated by Django 5.0.6 on 2024-08-25 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0010_remove_offeredservice_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offeredservice',
            name='services',
        ),
        migrations.AddField(
            model_name='offeredservice',
            name='expertises',
            field=models.ManyToManyField(related_name='offered_services', to='demo.expertise'),
        ),
        migrations.AddField(
            model_name='offeredservice',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='offered_services', to='demo.service'),
            preserve_default=False,
        ),
    ]
