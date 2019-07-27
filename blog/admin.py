from django.contrib import admin
from blog.models import Blog

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','body','blog_date')
admin.site.register(Blog,ProductAdmin)
