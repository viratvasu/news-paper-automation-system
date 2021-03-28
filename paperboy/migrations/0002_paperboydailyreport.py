# Generated by Django 3.0.8 on 2021-02-06 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paperboy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperboyDailyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('total_papers', models.IntegerField()),
                ('total_users', models.IntegerField()),
                ('deliveried_papers', models.IntegerField(blank=True, null=True)),
                ('deliveried_users', models.IntegerField(blank=True, null=True)),
                ('pprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paperboy.PaperboyProfile')),
            ],
        ),
    ]