from django.db import models
from fontawesome.fields import IconField
from datetime import datetime


# Create your models here.
class ShowcaseIntro(models.Model):
    name = models.CharField(max_length=200)
    job1 = models.CharField(max_length=200)
    job2 = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    icons = IconField()
    profession = models.CharField(max_length=200)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.profession


class About(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text


class Skill(models.Model):
    carreer = models.CharField(max_length=100)
    percentage = models.CharField(max_length=50)

    def __str__(self):
        return self.carreer


class Portfolio(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=250, blank=True)
    text = models.TextField(blank=True)
    client = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    completed_date = models.DateTimeField(blank=True)
    date_pub = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    quote = models.CharField(max_length=200, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    is_approved = models.BooleanField(default=False)
    date_create = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.full_name


class Footer(models.Model):
    site_about = models.CharField(max_length=300)
    street_num = models.CharField(max_length=100, blank=True)
    street_name = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    address_link = models.URLField(blank=True)
    twitter = IconField()
    instagram = IconField()
    github = IconField()
    linkedin = IconField()
    twi_link = models.URLField(blank=True)
    insta_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    java_link = models.URLField(blank=True)
    css_link = models.URLField(blank=True)
    html_link = models.URLField(blank=True)
    python_link = models.URLField(blank=True)
    php_link = models.URLField(blank=True)
