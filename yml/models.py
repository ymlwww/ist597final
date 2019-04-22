#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'test_pictures') 

    class Meta:
        db_table = "profile" 

    def __str__(self):
        return self.name

