# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


from .models import Article, ArticleComment, MenuItem
from .tools import yt_paginate, json_response
from .forms import CommentImageForm

# Create your views here.
def index(request):
	articles = Article.objects.all().order_by('-date').filter(isshow = True)
	articles = yt_paginate(articles, 
		per_page=15, 
		page_number=request.GET.get('page', 1))
	
	context = {
		"articles" : articles,
		"menuitems": MenuItem.objects.all(),
	}
	return render(request, "blog/index.html", context)

def category(request, pk):
	menuitem = get_object_or_404(MenuItem, pk = pk)
	articles = Article.objects.all().order_by('-date').filter(isshow = True, menu_item = menuitem)

	articles = yt_paginate(
        articles,
        per_page=15,
        page_number=request.GET.get('page', 1))

	context = {
		"articles" : articles,
		"menuitems": MenuItem.objects.all(),
		"typename" : menuitem.name
	}
	return render(request, "blog/index.html", context)

def article(request, pk):
	article = get_object_or_404(Article, pk = pk)
	article.watch_count += 1
	article.save()

	if request.POST:
		name = request.POST["name"]
		comment = request.POST["comment"]
		ArticleComment.objects.create(article = article, cname = name, comment = comment)

	comments = ArticleComment.objects.filter(article = article)\
										.order_by('-cdate')
	context = {
		"article" : article,
		"menuitems" : MenuItem.objects.all(),
		"comments" : comments
	}
	return render(request, "blog/article.html", context)

@csrf_exempt
@require_POST
@login_required
def upload_image(request):
    form = CommentImageForm(data=request.POST, files=request.FILES)

    if form.is_valid():
        image = form.save()
        return json_response({	'url': image.url, 
        						'message' : 'upload success!', 
        						'success' : 1
        					})
    return json_response({'error': dict(form.errors.items()), 'success' : 0})
