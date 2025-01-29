from django.urls import path
from .views import *

app_name='ib'

urlpatterns = [
    path("", index,name="home"),
    path("cover/<str:slug>/", insurance_cover, name="insurance_cover"),
    path("about-us", about_us, name="about_us")
]
