# 🛠 英辩赛事服务网站项目 - 开发者启动指南

## ✅ 开发准备

请在你的电脑安装以下内容：

- Python 3.10+
- Git
- VS Code（推荐）或任意代码编辑器

---

## 📥 克隆项目到本地

```bash
git clone https://github.com/PrimusXuan/BPWebsite
cd 你的仓库名
🧱 创建虚拟环境（只需第一次）
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate         # Windows
# 或 source venv/bin/activate（Mac/Linux）
📦 安装依赖
bash
Copy
Edit
pip install -r requirements.txt
🗃 初始化数据库
bash
Copy
Edit
python manage.py migrate
▶️ 启动开发服务器
bash
Copy
Edit
python manage.py runserver
打开浏览器访问：

cpp
Copy
Edit
http://127.0.0.1:8000/
📁 项目结构简览
bash
Copy
Edit
debate_service_website/
├── debate_platform/     # 主项目设置
├── templates/           # 页面模板
├── db.sqlite3           # SQLite数据库
├── manage.py            # 启动入口
├── requirements.txt     # 项目依赖
└── venv/                # 虚拟环境（不提交）
🔁 常用开发命令
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
⚠️ 注意事项
请勿将 venv/ 和 db.sqlite3 提交到 Git 仓库

每次开发前：记得激活虚拟环境 venv\Scripts\activate

每次开发后：记得提交代码 git add . && git commit -m "说明" && git push


