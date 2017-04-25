from django.db import models

# Create your models here.
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return '%s'%(self.name)


class Author(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64,default='123456')
    email = models.EmailField()

    def __str__(self):
        return '%s' % (self.name)


class Comments(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return '%s' % (self.headline)