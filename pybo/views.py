from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("도죠! pybo에 온걸 아카리마스~!")
# Create your views here.
