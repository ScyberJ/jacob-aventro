from django.shortcuts import render
from .models import Solution

# Create your views here.
def index(request):
    solutions = Solution.objects.all()
    return render(request, "edge_home.html", context={"solutions": solutions})

def about_us(request):
    return render(request, 'edge_about_us..html')

def solution_page(request, slug):
    solution = Solution.get_instance_from_slug(slug)

    return render(request, 'service_page.html', context={'solution': solution})
