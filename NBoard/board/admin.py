from django.contrib import admin
from .models import Ad, Response

class AdAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'text', 'category', 'dt_create', 'isnew',)
    list_filter = ('author', 'category', 'dt_create', 'isnew',)
    search_fields = ('title', 'text',)

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user', 'ad', 'text', 'dt_create', 'accept',)
    list_filter = ('user', 'ad', 'dt_create', 'accept',)
    search_fields = ('user', 'text', 'tad',)

admin.site.register(Ad, AdAdmin)
admin.site.register(Response, ResponseAdmin)






