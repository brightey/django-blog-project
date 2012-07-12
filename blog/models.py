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
	def body_first_60(self):
        	return self.body[:60]

class Comment(models.Model):
	body=models.TextField()
	author= models.CharField(max_length=60)
	date_created=models.DateField()
	last_updated=models.DateField()
	post=models.ForeignKey(Post, related_name='comments')
        def  __unicode__(self):
		return self.author

        def body_first_60(self):
        	return self.body[:60]
	



class PostAdmin(admin.ModelAdmin):
	list_display=('title','date_created','last_updated')
	search_fields=('title','body')
	list_filter =('date_created','title')
	
class PostInline(admin.TabularInline):
	model = Post
class AuthorAdmin(admin.TabularInline):
	inlines =[PostInline]
	



class CommentAdmin(admin.ModelAdmin):
	list_display=('post','author','body_first_60','date_created','last_updated')
	list_filter=('date_created','author')



class CommentInline(admin.TabularInline):
	model=Comment
class AuthorAdmin(admin.TabularInline):
	inlines=[CommentInline]
		



admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
#admin.site.register()
#admin.site.register()
