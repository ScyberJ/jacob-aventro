from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    pass

