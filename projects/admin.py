from django.contrib import admin

from .models import Project, Category

from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    pass
    summernote_fields = ('description',)


class CategoryAdmin(admin.ModelAdmin):

    pass


admin.site.register(Project, PostAdmin)
admin.site.register(Category, CategoryAdmin)
