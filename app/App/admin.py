from django.contrib import admin
from .models import Quiz
# Register your models here.

@admin.register(Quiz)
class CategoriesAdmin(admin.ModelAdmin):
    pass