from django.contrib import admin
from .models import Post
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('exercise_title', 'slug', 'status', 'created_on',)
    list_filter = ('status',)
    search_fields = ['exercise_title', 'body']
    prepopulated_fields = {'slug': ('exercise_title',)}
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ( 'approved','created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
admin.site.register(Comment, CommentAdmin)
