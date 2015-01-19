from django.shortcuts import render
import requests

def index(request):
    context = {
        'stories': [1,2,3]
    }
    return render(request, "feedlypop/index.html", context)
