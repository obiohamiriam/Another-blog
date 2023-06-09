from django.contrib import admin
from.models import Post

# Register your models here.
#dmin.site.register(Post)
"""We are telling the Django administration site that the model is registered inthe site using a custom class that inherits 
from ModelAdmin. In this class, we can  include information about how to display the model on the site and how to interact with it."""
@admin.register(Post)
class PostAdmin (admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields =['title', 'body']
    prepopulated_fields = {'slug' : ('title', )}
    