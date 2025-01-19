from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about-us', about_us, name='about_us'),
    path('contact-us', contact_us, name='contact_us'),
    path("solution/<str:slug>", solution_page, name='solution'),
]


