# Generated by Django 4.1.5 on 2023-01-22 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='bank',
            field=models.CharField(choices=[('Access Bank', 'Access Bank'), ('Fidelity Bank', 'Fidelity Bank'), ('First City Monument Bank', 'First City Monument Bank'), ('Zenith Bank', 'Zenith Bank'), ('Wema Bank', 'Wema Bank')], max_length=200),
        ),
    ]
