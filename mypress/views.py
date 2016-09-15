from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import post

def index(request):
    post_details = post.objects.filter(id='1')
    all_posts = post.objects.all()
    context = {
        'post' : post_details,
        'allposts' : all_posts
    }
    template = loader.get_template('blog/footer.html');
    return HttpResponse(template.render(context,request))


def posts(request,post_id):
    post_details = post.objects.get(pk=post_id)
    all_posts = post.objects.all()
    context = {
        'post' : post_details,
        'allposts' : all_posts,
    }
    template = loader.get_template('blog/footer.html');
    return HttpResponse(template.render(context,request))
