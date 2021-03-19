# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'modified_time', 'category', '__str__')

    # 过滤器
    list_filter = ['created_time']
    # 搜索功能
    search_fields = ['body']
    # 按id降序排列
    ordering = ('-pk',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TageAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TageAdmin)
admin.site.register(Post, PostAdmin)

admin.site.site_header = '蓝猫Admin'
