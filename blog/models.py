from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
	title= models.CharField(max_length=60)
	body=  models.TextField()
        date_created= models.DateField()
	last_updated= models.DateField()
	def  __unicode__(self):
	        return self.title
class Comment(models.Model):
	body=models.TextField()
	author= models.CharField(max_length=60)
	date_created=models.DateField()
	last_updated=models.DateField()
	Post=models.ForeignKey(Post)




admin.site.register(Post)
admin.site.register(Comment)
