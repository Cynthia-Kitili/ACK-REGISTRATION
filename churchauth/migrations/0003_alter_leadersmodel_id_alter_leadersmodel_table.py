# Generated by Django 4.0.2 on 2022-02-28 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchauth', '0002_leadersmodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadersmodel',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='leadersmodel',
            table='LeadersModel',
        ),
    ]