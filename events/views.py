from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/event_list.html', {'events': events})

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    
    return render(request, 'events/register.html', {'form': form})

def registration_success(request):
    return render(request, 'events/success.html')

#赛事详情视图函数
from django.shortcuts import get_object_or_404
from .models import Event

def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

#赛事专属报名视图
def register_specific(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event  # 自动绑定当前赛事
            registration.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
        form.fields['event'].initial = event.id
        form.fields['event'].widget = forms.HiddenInput()

    return render(request, 'events/register.html', {'form': form, 'event': event})

#赛事报名成功视图
def registration_success(request):
    return render(request, 'events/success.html', {'message': "你已成功报名！"})

#添加 “查看我的报名” 视图
from .models import Registration

def my_registrations(request):
    email = request.GET.get('email')  # 通过 URL 获取邮箱
    registrations = []

    if email:
        registrations = Registration.objects.filter(email=email).order_by('-registered_at')

    return render(request, 'events/my_registrations.html', {
        'registrations': registrations,
        'email': email
    })

# 👇 处理用户上传辩论稿件的视图：显示表单、接收数据、存入数据库、跳转成功页
from django.shortcuts import render, redirect
from .forms import ManuscriptForm

def upload_manuscript(request):
    if request.method == 'POST':
        # 表单中包含上传的文件，所以要传 request.FILES
        form = ManuscriptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # 保存到数据库
            return redirect('manuscript_success')  # 跳转成功页面
    else:
        form = ManuscriptForm()
    
    return render(request, 'events/upload_manuscript.html', {'form': form})

# ✅ 上传成功提示页
def manuscript_success(request):
    return render(request, 'events/manuscript_success.html')

# 👇 用户查看我的稿件视图：显示表单、接收邮箱、查询数据库、返回结果
from .models import Manuscript

# 👤 用户查看我的稿件视图
def my_manuscripts(request):
    manuscripts = None
    email = ''

    if request.method == 'POST':
        email = request.POST.get('email')
        manuscripts = Manuscript.objects.filter(email=email)

    return render(request, 'events/my_manuscripts.html', {
        'manuscripts': manuscripts,
        'email': email
    })


