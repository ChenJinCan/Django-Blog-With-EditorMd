# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template
from django.template.defaultfilters import stringfilter
from django.template.loader import render_to_string
from django.core.paginator import Page

register = template.Library()  #自定义filter时必须加上


@register.simple_tag(takes_context=True)
def render_paginator(context, page, page_var='page', hashtag=''):
    query_dict = context["request"].GET.copy()

    try:
        del query_dict[page_var]
    except KeyError:
        pass

    extra_query = ""

    if query_dict:
        extra_query = "&%s" % query_dict.urlencode()

    if hashtag:
        hashtag = "#%s" % hashtag

    new_context = {
        "page": page,
        "page_var": page_var,
        "hashtag": hashtag,
        "extra_query": extra_query
    }

    template = "blog/_footer.html"
    return render_to_string(template, new_context)