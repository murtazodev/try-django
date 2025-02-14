from django.contrib import admin
from .models import Recipe, RecipeIngredient

admin.site.register(RecipeIngredient)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    readonly_fields = ['quantity_float']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user']
    readonly_fields = ['created_at', 'updated_at']
    raw_id_fields = ['user']

admin.site.register(Recipe, RecipeAdmin)

    
