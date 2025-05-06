from django.contrib import admin
from .models import Event, Registration, Manuscript

admin.site.register(Event)
admin.site.register(Registration)

#增加 Manuscript 模型的 admin 注册，把 Manuscript 模型添加到后台管理系统中，这样在访问 /admin/ 后台页面时，就可以看到「稿件」这一项了
from django.contrib import admin
from .models import Manuscript

# 将 Manuscript 模型注册到 Django admin 后台管理系统中，允许管理员在后台查看和管理 Manuscript 模型的实例。
admin.site.register(Manuscript)

# 👇 自定义后台显示方式：让稿件信息在 Django admin 中更清晰易用
class ManuscriptAdmin(admin.ModelAdmin):
    # 后台列表中要显示的字段列
    list_display = ('name', 'email', 'service_type', 'submitted_at', 'is_reviewed')

    # 右侧的筛选器（Filter）：按服务类型 & 是否已处理筛选
    list_filter = ('service_type', 'is_reviewed')

    # 支持后台顶部搜索：按姓名或邮箱查找稿件
    search_fields = ('name', 'email')

    # 哪些字段是只读的（不能修改）
    readonly_fields = ('submitted_at',)
