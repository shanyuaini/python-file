from django.contrib import admin
from webchat import models
# Register your models here.

class WebGroupAdmin(admin.ModelAdmin):
    list_display = ('name','brief')


admin.site.register(models.WebGroup,WebGroupAdmin)