from django.contrib import admin
from .models import*

admin.site.register(RecipeIngredient)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    readonly_fields = ['user', 'created_at', 'updated_at']

admin.site.register(Recipe, RecipeAdmin)

    
