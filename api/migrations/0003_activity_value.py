# Generated by Django 3.1.7 on 2021-04-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_account_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='value',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]