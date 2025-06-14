# Generated by Django 5.2 on 2025-05-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manuscript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('file', models.FileField(upload_to='uploads/')),
                ('service_type', models.CharField(choices=[('ai', 'AI 改稿'), ('coach', '教练指导')], max_length=10)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
