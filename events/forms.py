from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'event']

# 📄 用户稿件上传表单：绑定 Manuscript 模型，供前端页面使用

from django import forms
from .models import Manuscript

class ManuscriptForm(forms.ModelForm):
    class Meta:
        model = Manuscript  # 表单绑定的模型
        fields = ['name', 'email', 'file', 'service_type']  # 显示的字段
