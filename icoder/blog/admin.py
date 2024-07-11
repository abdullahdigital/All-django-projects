""" from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((BlogComment))
@admin.register(Post)


class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',) """

from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models  # Import models module from Django
from .models import Post, BlogComment

# Register BlogComment model
admin.site.register(BlogComment)

# Define PostAdmin with TinyMCE integration for content field
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

# Register Post model with PostAdmin options
admin.site.register(Post, PostAdmin)




""" from django.contrib import admin
from blog.models import Post, BlogComment

admin.site.register((Post, BlogComment)) """