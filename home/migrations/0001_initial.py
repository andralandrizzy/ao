# Generated by Django 2.2.3 on 2019-07-12 02:58

import datetime
from django.db import migrations, models
import fontawesome.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_about', models.CharField(max_length=300)),
                ('street_num', models.CharField(blank=True, max_length=100)),
                ('street_name', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('address_link', models.URLField(blank=True)),
                ('twitter', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('instagram', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('github', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('linkedin', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('twi_link', models.URLField(blank=True)),
                ('insta_link', models.URLField(blank=True)),
                ('github_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('java_link', models.URLField(blank=True)),
                ('css_link', models.URLField(blank=True)),
                ('html_link', models.URLField(blank=True)),
                ('python_link', models.URLField(blank=True)),
                ('php_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('text', models.TextField(blank=True)),
                ('client', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
                ('completed_date', models.DateTimeField(blank=True)),
                ('date_pub', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icons', fontawesome.fields.IconField(blank=True, max_length=60)),
                ('profession', models.CharField(max_length=200)),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShowcaseIntro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('job1', models.CharField(max_length=200)),
                ('job2', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carreer', models.CharField(max_length=100)),
                ('percentage', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(blank=True, max_length=200)),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('is_approved', models.BooleanField(default=False)),
                ('date_create', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
