from django.contrib import admin
from forum.models import Category, Post, UserProfile

# Register your models here.

#helps to automatic slugify names
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    
#This helps displays topic, category and comment in the admin panel
class PostAdmin(admin.ModelAdmin):
    list_display =('topic', 'category', 'comment', 'likes')
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)