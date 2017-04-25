from django.contrib import admin
from blog import models

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name','tagline',)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','email','password',)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id','headline','body_text','pub_date','mod_date',)
    filter_horizontal = ('authors',)

admin.site.register(models.Author,AuthorAdmin)
admin.site.register(models.Blog,BlogAdmin)
admin.site.register(models.Comments,CommentsAdmin)