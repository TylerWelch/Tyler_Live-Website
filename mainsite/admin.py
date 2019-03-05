from django.contrib import admin
from .models import BlogPost, PortfolioPost
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
	fieldsets = [
        ("Title/date", {'fields': ["title", "date_posted"]}),
        ("Content", {"fields": ["content", "blogimage"]})
    ]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
		}

class PortfolioPostAdmin(admin.ModelAdmin):
	fieldsets = [
        ("Title/date", {'fields': ["port_title", "port_description", "port_date_posted"]}),
        ("Content", {"fields": ["port_content", "port_image"]})
    ]

	formfield_overrides = {
		models.TextField: {'widget': TinyMCE()}
		}


admin.site.register(BlogPost, BlogPostAdmin) 
admin.site.register(PortfolioPost, PortfolioPostAdmin)

