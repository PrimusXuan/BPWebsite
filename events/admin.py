from django.contrib import admin
from .models import Event, Registration, Manuscript

# ✅ 注册 Event 模型（简单注册方式）
admin.site.register(Event)

# ✅ 使用装饰器方式注册 Registration，并自定义管理界面
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'registered_at', 'is_confirmed')
    list_filter = ('is_confirmed',)
    search_fields = ('name', 'email')

# ✅ 使用装饰器方式注册 Manuscript，并自定义管理界面
@admin.register(Manuscript)
class ManuscriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service_type', 'submitted_at', 'is_reviewed')
    list_filter = ('service_type', 'is_reviewed')
    search_fields = ('name', 'email')
    readonly_fields = ('submitted_at',)
