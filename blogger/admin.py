from django.contrib import admin
from .models import Blogger, Category

admin.site.site_header = 'Bloggers Admin'

class BloggerAdmin(admin.ModelAdmin):
	list_display = ('title', 'topic', 'author')


admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Category)
