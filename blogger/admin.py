from django.contrib import admin
from .models import Blogger

admin.site.site_header = 'Bloggers Admin'

class BloggerAdmin(admin.ModelAdmin):
	list_display = ('title', 'topic', 'auther')


admin.site.register(Blogger, BloggerAdmin)
