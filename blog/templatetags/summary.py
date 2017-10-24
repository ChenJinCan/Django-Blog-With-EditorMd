#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from django import template
from django.template.defaultfilters import stringfilter
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def get_summary(text):
    limit_length = 250
    length = len(text)
    if length > limit_length:
        length = limit_length
    string = text[0:length - 1]
    string = string.replace('#', '')
    string = string.replace('\'', '')
    count = string.count("```")
    if count % 2 != 0 :
    	string += "```"
    return mark_safe(string)

