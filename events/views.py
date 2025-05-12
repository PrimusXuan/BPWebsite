# ------------------------------------
# 📦 通用导入
# ------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration, Manuscript
from .forms import RegistrationForm, ManuscriptForm

# ------------------------------------
# 📅 赛事模块：展示赛事列表 + 报名
# ------------------------------------

# 展示所有赛事
def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events/event_list.html', {'events': events})

# 赛事详情页
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# 报名任意赛事（通用）
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'events/register.html', {'form': form})

# 报名指定赛事
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

# 报名成功页
def registration_success(request):
    return render(request, 'events/success.html', {'message': "你已成功报名！"})

# ------------------------------------
# 📨 用户查询模块：我的赛事报名 / 我的稿件
# ------------------------------------

# 查看我的赛事报名
def my_registrations(request):
    email = request.GET.get('email')  # 通过 URL 获取邮箱
    registrations = Registration.objects.filter(email=email).order_by('-registered_at') if email else []
    return render(request, 'events/my_registrations.html', {
        'registrations': registrations,
        'email': email
    })

# 查看我的上传稿件
def my_manuscripts(request):
    email = ''
    manuscripts = None
    if request.method == 'POST':
        email = request.POST.get('email')
        manuscripts = Manuscript.objects.filter(email=email)
    return render(request, 'events/my_manuscripts.html', {
        'manuscripts': manuscripts,
        'email': email
    })

# 查看我的个人信息
# 这里可以根据需求添加用户信息的展示
# 例如：用户的基本信息、报名记录等
def my_dashboard(request):
    return render(request, 'events/my_dashboard.html')


# ------------------------------------
# 📤 稿件上传模块
# ------------------------------------

# 上传辩论稿
def upload_manuscript(request):
    if request.method == 'POST':
        form = ManuscriptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manuscript_success')
    else:
        form = ManuscriptForm()
    return render(request, 'events/upload_manuscript.html', {'form': form})

# 上传成功页
def manuscript_success(request):
    return render(request, 'events/manuscript_success.html')
