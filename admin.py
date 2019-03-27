from django.contrib import admin
from .models import Category, Product, SocialApplication, Clients


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SocialApplication)
class SocialApplicationAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug']
    prepopulated_fields = {'slug': ('last_name',)}
