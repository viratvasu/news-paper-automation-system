# Generated by Django 3.0.8 on 2021-02-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
