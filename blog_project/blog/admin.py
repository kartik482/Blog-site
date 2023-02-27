from django.contrib import admin
from . models import Post, Blogcomment


# Register your models here.
# admin.site.register(Post)    not applicable for tinymce
admin.site.register(Blogcomment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=("tinyinject.js",)
