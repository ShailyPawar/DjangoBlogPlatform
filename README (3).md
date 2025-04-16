# Django Blog 📝

This is a simple blog application built using Django. It allows users to browse blog posts with a clean UI, and provides admin functionalities to add, update, and delete posts.

## 🚀 Features

- Dynamic blog post listing
- Individual post pages
- Admin panel with full CRUD support
- Bootstrap-based responsive UI
- Pagination of posts

## 🛠 Tech Stack

- Django
- SQLite (default)
- Bootstrap 4

## 🔧 Setup Instructions

```bash
git clone https://github.com/your-username/django-blog.git
cd django-blog
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 👤 Admin Panel

Visit: http://127.0.0.1:8000/admin/

## 📄 License

This project is licensed under the MIT License.