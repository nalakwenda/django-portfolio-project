from django.db import models
from taggit.managers import TaggableManager


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    image =models.ImageField(upload_to='images')
    categories = models.ManyToManyField("Category", related_name="project")
    technology = TaggableManager()
    created_on = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    name = models.CharField(max_length=20)
