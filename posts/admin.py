

"""Posts model."""

# Django
from django.contrib import admin

# Models
from posts.models import Post

# Register your models here.
@admin.register(Post) # Decorador
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'photo')

    fieldsets = (
        ('Post!',{
            'fields':(('user', 'title'),('profile','photo'),) # Antes tenía un error no me dejaba postear por que no adicioné 'profile' a la tupla de 'fields'
            }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
            }),
        )
    readonly_fields = ('created', 'modified')




    '''' La manera sencilla: '
    """Posts model."""

# Django
from django.contrib import admin

# Models
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin."""

    list_display = ('id', 'user', 'title', 'photo')
    search_fields = ('title', 'user__username', 'user__email')
    list_filter = ('created', 'modified')'''
