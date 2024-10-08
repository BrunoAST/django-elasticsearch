# Generated by Django 5.0.6 on 2024-06-16 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_remove_offeredservice_service_provider_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='offered_services',
        ),
        migrations.AddField(
            model_name='offeredservice',
            name='service_provider',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='offered_services', to='demo.serviceprovider'),
            preserve_default=False,
        ),
    ]
