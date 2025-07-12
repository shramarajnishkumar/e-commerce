from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(product)
@admin.register(models.Register)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','address']

@admin.register(models.Contact)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','message','enq_time']

@admin.register(models.Review)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','message','product','date']

admin.site.register(models.Cart)
admin.site.register(models.Order)



