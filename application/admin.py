from django.contrib import admin

from .models import UserTable, Like, PostBlog
# Register your models here.

class UserTableDisplay(admin.ModelAdmin):
    list_display = ["user_id", "name", "email", "status" ]

class PostBlogDisplay(admin.ModelAdmin):
    list_display = ["user_id", "post_id", "title", "description", "content" ]

class LikeDisplay(admin.ModelAdmin):
    list_display = ["user_id", "post_id", "like_id", "like_status"]

admin.site.register(UserTable, UserTableDisplay)
admin.site.register(PostBlog, PostBlogDisplay)
admin.site.register(Like, LikeDisplay)