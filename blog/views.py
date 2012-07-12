"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response


from models import Post, Comment 


def post_list(request,):
   # html=''
	posts = Post.objects.all()
   
    #for p in post_list:
     #   html+='<p>'+'<h1>' + str(p) +'</p>' + '</h1>'+'<p>'+ p.body + '</p>'
     #   return HttpResponse(html) 
	t = loader.get_template('blog/post_list.html')
	c = Context({'posts': posts})
	return HttpResponse(t.render(c))			
    
  #  print type(post_list)
   # print post_list
    
   # return HttpResponse('This should be a list of posts!')

def post_detail(request, id, showComments=False):
        html=''    
	single_post=Post.objects.get(pk=id)
        html+='<p>'+'<h2>' +str(single_post) + '</h2>'+'</p>'+'<p>'+single_post.body+'</p>'
	comment_blog=''
	if showComments!= False:
		for k in single_post.comments.all():
    			comment_blog+=k.body +'<br/>'
	return HttpResponse(html + comment_blog)

def post_search(request, term):
	p = Post.objects.all()
	search = ''
	for i in p:

		search += i.filter(body__contains=term)
	
	return HttpResponse(search)
	
   

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') # Create your views here.
