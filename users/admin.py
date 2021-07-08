"""User admin classes"""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from users.models import Profile

from django.contrib.auth.models import User

# Register your models here.
@admin.register(Profile) # Decorador

class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    # pass
    list_display = ('pk','user', 'website', 'biography', 'phone_number', 'picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website', 'picture')
    
    search_fields = (
        'user__email',
        'user__name'
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        
        ('Profile', {
            'fields':(
                'user', 
                'picture'
                ),
            }),
        ('Extra Info!', {
            'fields': ((
                'website',
                'phone_number',),
                ('biography'),

            )}),
            
            ('Metadata', { 
                'fields':(
                    'created',
                    'modified',
                    )
                }),

    )
    
    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'



class UserAdmin(BaseUserAdmin):
    """Add profile  admin to base user admin."""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


        