from django.shortcuts import render
from .models import Solution
from .forms import ContactForm

# Create your views here.
def index(request):
    solutions = Solution.objects.all()
    return render(request, "edge_home.html", context={"solutions": solutions})

def about_us(request):
    return render(request, 'edge_about_us..html')

def solution_page(request, slug):
    solution = Solution.get_instance_from_slug(slug)

    return render(request, 'service_page.html', context={'solution': solution})

def contact_us(request):
    form = ContactForm()


    if request.POST:
        form = ContactForm(request.POST)

        pass
    
    return render(request, 'contact_page.html', context={"form": form})