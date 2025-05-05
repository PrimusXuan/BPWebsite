"""
URL configuration for debate_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),  # 👈 绑定子路由, 设置首页
]

# 导入 Django 的媒体文件工具
from django.conf import settings
from django.conf.urls.static import static

# 添加媒体文件访问配置
# 作用：让 /media/xxx 请求能读取到 media 文件夹里的真实文件（开发环境用）
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

