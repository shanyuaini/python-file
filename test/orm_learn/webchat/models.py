from django.db import models

# Create your models here.

from bbs.models import UserProfile
class WebGroup(models.Model):
    name = models.CharField(max_length=64)
    brief = models.CharField(max_length=255,blank=True,null=True)
    owner = models.ForeignKey(UserProfile)
    admins = models.ManyToManyField(UserProfile,blank=True,related_name='group_admins')
    members = models.ManyToManyField(UserProfile,blank=True,related_name='group_members')
    max_members = models.IntegerField(default=200)
    def __str__(self):
        return self.name