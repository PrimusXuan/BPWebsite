from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('register/', views.register, name='register'),
    path('success/', views.registration_success, name='registration_success'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/register/', views.register_specific, name='register_specific'),
    path('my-registrations/', views.my_registrations, name='my_registrations'),
    path('manuscripts/upload/', views.upload_manuscript, name='upload_manuscript'),  # 📤 用户上传稿件页面
    path('manuscripts/success/', views.manuscript_success, name='manuscript_success'),  # ✅ 成功提示页
    path('my-manuscripts/', views.my_manuscripts, name='my_manuscripts'), # 📜 查看我的稿件
    path('my-registrations/', views.my_registrations, name='my_registrations'), # 📋 查看我的赛事报名
    path('my/', views.my_dashboard, name='my_dashboard'), # 👤 查看我的个人信息



]


