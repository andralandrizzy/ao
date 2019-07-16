from django.contrib import admin
from . models import Author, Category, Blog, Comment
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_publish')
    list_display_links = ('id', 'title', 'date_publish')
    list_filter = ('title', 'date_publish')
    search_fields = ('title', 'date_publish')
    list_per_page = 25


admin.site.register(Blog, BlogAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job',)
    list_display_links = ('name', 'email', 'job',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Author, AuthorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'tags')
    list_display_links = ('id', 'tags',)
    list_filter = ('tags',)
    search_fields = ('tags',)
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'approved_comment', 'first_name',
                    'last_name', 'email', 'created_date')
    list_display_links = ('id', 'approved_comment',
                          'first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name', 'email', 'approved_comment')
    search_fields = ('first_name', 'last_name', 'email', 'approved_comment')
    list_per_page = 25


admin.site.register(Comment, CommentAdmin)
