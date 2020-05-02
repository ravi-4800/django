from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	pass

class PostAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'body']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
