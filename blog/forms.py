# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os

from django import forms
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_bytes

from .tools import get_file_hash

class CommentImageForm(forms.Form):

    editormd_image_file = forms.ImageField(_("editormd_image_file"))

    def __init__(self, *args, **kwargs):
        super(CommentImageForm, self).__init__(*args, **kwargs)

    def clean_image(self):
        file = self.cleaned_data['editormd_image_file']

        if file.image.format.lower() not in settings.ALLOWED_UPLOAD_IMAGE_FORMAT:
            raise forms.ValidationError(
                _("Unsupported file format. Supported formats are %s."
                  % ", ".join(settings.ALLOWED_UPLOAD_IMAGE_FORMAT))
            )
        return file

    def save(self):
        file = self.cleaned_data['editormd_image_file']
        file_hash = get_file_hash(file)
        file.name = ''.join((file_hash, '.', file.image.format.lower()))
        name = os.path.join('images', file.name)
        name = default_storage.save(name, file)
        file.url = default_storage.url(name)
        return file
