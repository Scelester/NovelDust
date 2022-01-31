from django.contrib import admin

# Register your models here.
from .models import TopBooks,BookItems,Genrelist,Author
admin.site.register(TopBooks)
admin.site.register(BookItems)
admin.site.register(Genrelist)
admin.site.register(Author)