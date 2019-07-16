from django.db import models
from datetime import datetime
from fontawesome.fields import IconField

# Create your models here.


class Author(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    job = models.CharField(max_length=100, blank=True)
    info = models.CharField(max_length=260, blank=True)
    facebook = IconField()
    twitter = IconField()
    instagram = IconField()
    github = IconField()
    link1 = models.URLField(blank=True)
    link2 = models.URLField(blank=True)
    link3 = models.URLField(blank=True)
    link4 = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    tags = models.CharField(max_length=150)

    def __str__(self):
        return self.tags


class Blog(models.Model):
    image = models.ImageField(upload_to="photos/%Y/%m/%d/")
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_publish = models.DateTimeField(default=datetime.now, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    Post = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.comment_text
