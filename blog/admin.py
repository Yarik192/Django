from django.contrib import admin
from blog.models import User, Comment, ReplyToComment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["nickname"]


@admin.register(Comment)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ReplyToComment)
class ReplyToCommentAdmin(admin.ModelAdmin):
    pass
