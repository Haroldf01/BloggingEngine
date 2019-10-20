from django.contrib import admin
from .models import Blogger

admin.site.site_header = 'Bloggers Admin'
admin.site.register(Blogger)

class BloggerAdmin(admin.ModelAdmin):
	list_display = ('title', 'topic', 'writer')
