from django.contrib import admin

from users.models import Product, User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'phone', 'role']
    search_fields = ['name', 'email', 'phone']
    list_filter = ['role']

admin.site.register(User, UserAdmin)
