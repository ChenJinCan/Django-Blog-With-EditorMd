# Django-Blog-With-EditorMd
Blog in Django, Integration with Editor.md, Simple Menu and Comment. 

### Features
1. Edit Admin with [editor.md](https://github.com/pandao/editor.md), You Can use All Editor.Md Features!
![](https://github.com/ChenJinCan/Django-Blog-With-EditorMd/blob/master/introduction/you_can_editor_in_admin.png)

2. Show Markdown In Blog.
![](https://github.com/ChenJinCan/Django-Blog-With-EditorMd/blob/master/introduction/Show%20Markdown%20In%20Blog.png)

3. Simple & Useful Menu.
4. Simple Comment Component.
![](https://github.com/ChenJinCan/Django-Blog-With-EditorMd/blob/master/introduction/Comment.png)

### Prepare
1. Install Python2 or Python3
2. Install pip
3. Install Django >= 1.10
```shell
pip install django
```

4. Install Pillow
```shell
pip install pillow
```

5. Run Demo
```shell
python manager.py runserver 80
```

6. Visit [127.0.0.1](http://127.0.0.1) , Then You Can See Full Demo!

### Expand Yourself
#### 1. You can only use editormd as an app. And Use Django formfield_overrides to make Editor.md valid.Just like this:

```python
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
```

#### 2. You can expend menu item at django-admin。
![](https://github.com/ChenJinCan/Django-Blog-With-EditorMd/blob/master/introduction/add_menu_item.png)

