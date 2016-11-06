from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def start(req):
    context={}
    return render(req, 'ydy_web/start.html', context)
    #return HttpResponse("<h1>start_page</h1>")
def sign_in(req):
    return HttpResponse("<h1>sing_in_page</h1>")
def sign_up(req):
    return HttpResponse("<h1>sing_up_page</h1>")