from django.contrib import admin
from .models import Profile, Customer

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email_confirmed', 'is_admin']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'address', 'locality', 'created_at']