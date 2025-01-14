from django.contrib import admin
from .models import Cover

# Register your models here.
@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    pass


