from django.contrib import admin

from .models import Product,Category,Address,Company


# Example

class stackproduct(admin.StackedInline):
    model=Product
    extra=0

class tbularcompany(admin.TabularInline):
    model=Product
    extra=0

@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'price']
    list_filter=['category','company']
    sortable_by=['price']
    list_display_links=['id','name']

# Add the rest of admin models here
@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    inlines=[stackproduct]

@admin.register(Address)
class Addressadmin(admin.ModelAdmin):
    list_display=['postal_address','city']
    list_filter=['city']

@admin.register(Company)
class Companyadmin(admin.ModelAdmin):
    inlines=[tbularcompany]

