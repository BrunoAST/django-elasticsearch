# Generated by Django 5.0.6 on 2024-08-19 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_alter_category_options_alter_expertise_service_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offeredservice',
            name='service',
        ),
        migrations.AddField(
            model_name='offeredservice',
            name='services',
            field=models.ManyToManyField(related_name='offered_services', to='demo.service'),
        ),
    ]
