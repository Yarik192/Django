from django.contrib import admin
from blog.models import User, Article, ReplyToComment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["nickname"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ReplyToComment)
class ReplyToCommentAdmin(admin.ModelAdmin):
    pass
