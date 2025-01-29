from django.shortcuts import render

from general.forms import ContactForm

# Create your views here.
def contact_us(request):
    form = ContactForm()


    if request.POST:
        form = ContactForm(request.POST)

        pass
    
    return render(request, 'contact_page.html', context={"form": form})