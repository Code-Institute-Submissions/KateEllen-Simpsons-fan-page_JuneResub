from django.contrib import admin
from .models import Post, Comment, Characters
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_filter = ('status', 'created_on', 'title')
    search_fileds = ['title', 'content']
    summernote_fields = ('content')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fileds = ('name', 'email', 'body')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        
@admin.register(Characters)
class CharacterAdmin(admin.ModelAdmin):
    list_filter = ()