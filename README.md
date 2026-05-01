# django-practice2 — Practical practice done by me
# 🚀 Django Beginner Guide

![Django](https://img.shields.io/badge/Django-Framework-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Learning-orange)

> A complete beginner-friendly guide to building your first Django project.

---

## 📌 Table of Contents

- Installation
- Create Project
- Migrations
- Create App
- Connect App
- Views & URLs
- Templates
- Static Files
- Media Files
- Navigation
- Notes

---
## 📦 Installation

```bash
pip install django
```
---
## Check Version

```bash
django-admin --version
```
---
## 🏗️ Create Project

```bash
django-admin startproject project_name
cd project_name
```

---
## Run Server

```bash
python manage.py runserver
```
---
## Stop Server

```bash
Ctrl + C
```
---
## 🔄 Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
⚠️ Always run makemigrations before migrate

---
## 📱 Create App

```bash
python manage.py startapp application_name
```

---
## 📁 Project Structure
```bash
project_folder/
 ├── project_name/
 ├── application_name/
 ├── manage.py
```
---

## 🔗 Connect App
#### Edit project_name/settings.py:
```bash
INSTALLED_APPS = [
    'application_name',
]
```

---
## 👀 First View
#### 📄 application_name/views.py
```bash
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is my first Django page!")
```
---
## 🌐 URLs Setup
#### 📄 App URLs → application_name/urls.py
```bash
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
<br>

#### 📄 Project URLs → project_name/urls.py
```bash
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('application_name.urls')),
    path('admin/', admin.site.urls),
]
```

---
## 🧾 Templates (HTML)
#### 📁 Create folder:
```bash
application_name/templates/
```
<br>

### 📄 home.html
```bash
<!DOCTYPE html>
<html>
<head>
    <title>Django</title>
</head>
<body>
    <h1>Hello from Django Template 🚀</h1>
</body>
</html>
```
<br>

### Update views.py:
```bash
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```
---

## ➕ Add Another Page
### 📄 views.py
```bash
def about(request):
    return render(request, 'about.html')
```
<br>

### 📄 urls.py
```bash
path('about/', views.about, name='about'),
```
<br>

### 📄 about.html
```bash
<h1>About Page</h1>
<p>This is my about page</p>
```
<br>

### 🔗 Link in home.html
```bash
<a href="/about/">Go to About Page</a>
```
<br>

---
## 🎨 Static Files (CSS, JS, Images)
### 📁 Project_Structure
```bash
static/
 ├── css/
 ├── js/
 ├── images/
 ```
<br>

 ### 📄 Usage
```bash
{% load static %}

<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/script.js' %}"></script>
<img src="{% static 'images/logo.png' %}">
```
<br>

### 🎥 Media (Image, Video, Audio)
```bash
<img src="{% static 'images/pic.png' %}" width="300">

<video controls>
    <source src="{% static 'videos/video.mp4' %}">
</video>

<audio controls>
    <source src="{% static 'audio/sound.mp3' %}">
</audio>
```
<br>

### 🔗 Navigation Example
```bash
<nav>
    <a href="{% url 'home' %}">Home</a> |
    <a href="{% url 'about' %}">About</a>
</nav>
```
--- 
🧠 Important Notes
- include() → only used in project urls.py
- Use / instead of \ in paths
- {% load static %} is required
- Templates render data using {{ }}

---
## Template Tags
```bash
| Purpose      | Syntax                  |
| ------------ | ----------------------- |
| Static files | `{% static %}`          |
| URL routing  | `{% url %}`             |
| Logic        | `{% if %}`, `{% for %}` |
| Variables    | `{{ variable }}`        |
```
---

## ⭐ Summary

- Project → settings.py, urls.py
- App → views.py, urls.py
- Templates → UI
- Static → Styling
---
<br>

## 🙌 Contributing
#### Feel free to fork this repo and improve it.
---
<br>

## 📄 License
#### This project is open-source and free to use.
---
<br>

### 👩‍💻 Author
#### Made with ❤️ for learning Django
<br>