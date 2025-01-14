from django.http import HttpRequest
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request: HttpRequest):
    covers = Cover.objects.all()
    return render(request, "index.html", context={"covers": covers})

def insurance_cover(request: HttpRequest, slug: str):
    cover = Cover.objects.get(name=Cover.slug_to_name(slug))
    return render(request, 'cover.html', context={"cover": cover})

def about_us(request):
    return render(request, "about_us.html")