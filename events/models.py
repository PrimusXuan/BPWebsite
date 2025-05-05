from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

#增加一个“用户识别”字段，比如 email
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

#创建模型 Manuscript，用户上传的辩论稿件信息，包括文件、服务类型、提交时间等
class Manuscript(models.Model):
    SERVICE_CHOICES = [
        ('ai', 'AI 改稿'),
        ('coach', '教练指导'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    file = models.FileField(upload_to='uploads/')
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_service_type_display()}"
