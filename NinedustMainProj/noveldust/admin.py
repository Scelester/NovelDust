from django.contrib import admin

# Register your models here.
from .models import TopBooks,BookItems,Genrelist
admin.site.register(TopBooks)
admin.site.register(BookItems)
admin.site.register(Genrelist)

class topbookInline(admin.TabularInline):
    model = TopBooks

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        topbookInline,
    ]