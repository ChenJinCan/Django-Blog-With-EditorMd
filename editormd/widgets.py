#coding:utf-8
from django import VERSION, forms
from django.contrib.admin import widgets as admin_widgets
from django.utils.html import conditional_escape
from django.template import Context, loader

try:
    from django.utils.encoding import force_unicode
except ImportError:  # python3
    from django.utils.encoding import force_text as force_unicode


def compatible_staticpath(path):
    try:
        # >= 1.4
        from django.templatetags.static import static
        return static(path)
    except ImportError:
        pass
    try:
        # >= 1.3
        return '%s/%s' % (settings.STATIC_URL.rstrip('/'), path)
    except AttributeError:
        pass
    try:
        return '%s/%s' % (settings.PAGEDOWN_URL.rstrip('/'), path)
    except AttributeError:
        pass
    return '%s/%s' % (settings.MEDIA_URL.rstrip('/'), path)

class EditormdWidget(forms.Textarea):
	def __init__(self, *args, **kwaargs):
		self._template = "editormd/editormd.html"
		super(EditormdWidget, self).__init__(*args, **kwaargs)

	def __media(self):
		return forms.Media(
		css = {
			"all" : (
				compatible_staticpath("editormd/css/editormd.css"),
				compatible_staticpath("editormd/css/editormd.preview.css"),
				compatible_staticpath("editormd/css/font-awesome.css"),
			),	
		}, 
		js = (
			compatible_staticpath("editormd/src/jquery.min.js"),
			compatible_staticpath("editormd/src/editormd.js"),
			compatible_staticpath("editormd/languages/en.js"),
		))
	media = property(__media)

	def render(self, name, value, attrs=None):
		if value is None:
			value = ""
		template = loader.get_template(self._template)

		context = {
			"body" : conditional_escape(force_unicode(value)),
		}
		return template.render(context)

class AdminEditormdWidget(EditormdWidget, admin_widgets.AdminTextareaWidget):
	pass
