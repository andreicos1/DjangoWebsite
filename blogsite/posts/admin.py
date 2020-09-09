from django.contrib import admin
from .models import Post, Comment
# Register your models here.
admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commenter', 'text', 'submited_on', 'active')
    list_filter = ('active', 'submited_on')
    actions =['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
