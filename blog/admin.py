# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

from .models import Article, MenuItem, ArticleComment
from editormd.widgets import AdminEditormdWidget

# Register your models here.
class AdminArticle(admin.ModelAdmin):
	formfield_overrides = {
		models.TextField : {'widget' : AdminEditormdWidget}
	}

admin.site.register(Article, AdminArticle)
admin.site.register(MenuItem)
admin.site.register(ArticleComment)