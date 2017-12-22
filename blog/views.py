from django.shortcuts import render
#
# HB added next lines in a second pass as per Dynamic Data in Templates
#
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

# HB added to publish posts sorted by publish_date
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# In the render function we have one parameter request 
# (everything we receive from the user via the Internet) 
# and another giving the template file ('blog/post_list.html'). 
# The last parameter, {}, is a place in which we can add some things 
# for the template to use. We need to give them names (we will stick to 'posts' right now).
# :) It should look like this: {'posts': posts}. Please note that the part before : 
# is a string; you need to wrap it with quotes: ''.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

