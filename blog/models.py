# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class MenuItem(models.Model):
	name = models.CharField(_("name"), max_length = 255)
	order = models.IntegerField(_("order id"))

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Article(models.Model):
	menu_item = models.ForeignKey(MenuItem, default = None)
	title = models.CharField(_("Title"), max_length = 255)
	author = models.CharField(_("Author"), max_length = 255, default = _("Admin"))
	date = models.DateTimeField(_("Date"), default=timezone.now)
	editormd = models.TextField(_("Editor md"))
	watch_count = models.IntegerField(_("Watch Count"), default=0)
	isshow = models.BooleanField(_("Is Show:"), default = True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _("article")
		verbose_name_plural = _("article")

@python_2_unicode_compatible
class ArticleComment(models.Model):
	article = models.ForeignKey(Article)
	cname = models.CharField(_("name"), max_length = 255)
	comment = models.TextField(_("comment"))
	cdate = models.DateTimeField(_("comment_date"), default = timezone.now)
	
	def __str__(self):
		return self.cname

	class Meta:
		verbose_name = _("article comment")
		verbose_name_plural = _("article comments")
	