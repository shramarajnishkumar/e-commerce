from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(User)

admin.site.register(Category)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile']
@admin.register(product)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','brand','category','price','active']