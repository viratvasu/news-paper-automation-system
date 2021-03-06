# Generated by Django 3.0.8 on 2021-02-06 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paperboy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('papers', models.ManyToManyField(to='accounts.NewsPaper')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adress', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Adress')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Branch')),
                ('paperboy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='paperboy.PaperboyProfile')),
                ('payment_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.PaymentProfile')),
                ('subscription', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.Subscription')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerDailyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_received', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('no_of_papers', models.IntegerField(blank=True, null=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.CustomerProfile')),
            ],
        ),
    ]
