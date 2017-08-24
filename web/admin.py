# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Ticker
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'author','text', 'published_date', 'created_date', 'updated_date', )
    readonly_fields = ('updated_date', 'created_date',)
    list_display = ('title', 'author', 'published_date', 'updated_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Ticker)