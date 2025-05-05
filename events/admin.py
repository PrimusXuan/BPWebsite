from django.contrib import admin
from .models import Event, Registration

admin.site.register(Event)
admin.site.register(Registration)

#增加 Manuscript 模型的 admin 注册，把 Manuscript 模型添加到后台管理系统中，这样在访问 /admin/ 后台页面时，就可以看到「稿件」这一项了
from django.contrib import admin
from .models import Manuscript

admin.site.register(Manuscript)
