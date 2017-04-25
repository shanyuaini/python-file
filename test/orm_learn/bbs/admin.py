from django.contrib import admin
from bbs import models

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','author','pub_date','mod_date','status')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','article','parent_comment','comment_type','comment','user','comm_date')
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','set_as_top','position_index')

admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Comment,CommentAdmin)
admin.site.register(models.Category,CategoryAdmin)
admin.site.register(models.UserProfile)