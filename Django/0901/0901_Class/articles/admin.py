from django.contrib import admin
from .models import Article

# Register your models here.

# admin.site.register(Article)

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'content', 'created_at', 'updated_at')

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'content', 'created_at', 'updated_at',)
#     list_display_links = ('content',) # 링크로 지정할 컬럼을 설정한다.
#     list_editable = ('title',)
#     list_per_page = 3

# admin.site.register(Article, ArticleAdmin)

# 모든 필드를 한번에 등록하고 싶다면? 일일이 타이핑x
# def get_all_fields(self):
#     return tuple(field.name for field in self._meta.get_fields())

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = get_all_fields(Article)

# # 2
class ArticleAdmin(admin.ModelAdmin):
    list_display = tuple(field.name for field in Article._meta.get_fields())

admin.site.register(Article, ArticleAdmin)