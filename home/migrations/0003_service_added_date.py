# Generated by Django 2.2.3 on 2019-10-10 02:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_portfolio_site_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='added_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
