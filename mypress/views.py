from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome To MyPress</h1>")
