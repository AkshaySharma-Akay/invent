from django.http import HttpResponse
from django.template import loader
from .models import post

def index(request):
    post_details = post.objects.filter(id='1')
    context = {
        'post' : post_details
    }
    template = loader.get_template('blog/post.html');
    return HttpResponse(template.render(context,request))
