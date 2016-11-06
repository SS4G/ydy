from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def start(req):
    context={}
    return render(req, 'ydy_web/start.html', context)
    #return HttpResponse("<h1>start_page</h1>")
def sign_in(req):
    context={}
    return render(req, 'ydy_web/sign_in.html', context)
    #return HttpResponse("<h1>sing_in_page</h1>")
def sign_up(req):
    context={}
    return render(req, 'ydy_web/sign_up.html', context)
    #return HttpResponse("<h1>sing_up_page</h1>")
def sign_up_result(req):
    return HttpResponse("<h1>sing_up_success</h1>")
def sign_in_result(req):
    return HttpResponse("<h1>sing_in_success</h1>")
    