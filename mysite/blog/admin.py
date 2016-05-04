from django.contrib import admin
from .models import Post, Comment, PostSection

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostSection)
# Register your models here.
