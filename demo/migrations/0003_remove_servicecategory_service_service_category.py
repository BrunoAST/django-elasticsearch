# Generated by Django 5.0.6 on 2024-06-16 16:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_serviceprovider_cnpj_alter_serviceprovider_cpf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicecategory',
            name='service',
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='demo.servicecategory'),
            preserve_default=False,
        ),
    ]
