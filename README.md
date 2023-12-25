# Django Lofter Project
Introduction:  
This is a long-blog website called 'Lofter', where you can register, login a user, and create your blogs, and view others' blogs. You can upload a cover image to your blogs, modify your profile info, upload an profile image. You can request for a password change email when you forget your password.  

This website is live on my virtual Ubuntu machine:  
[https://django-blog.sawyerguan.top/]("https://django-blog.sawyerguan.top/")  
On my virtual machine, I use Nginx and Gunicorn to serve this website, and set up Postgres as the DB for it. For this domain, I enable HTTPS using Let's Encrypt.

Technologies I use in this project:  
This website is built with Django, and the frontend is built with Bootstrap and plain CSS, HTML.
## Getting started
To run the website locally using sqlite3 as the DB, navigate to the 'django_project' directory, and build a venv on top of the requirements.txt, and run:
```
python manage.py migrate &&
python manage.py runserver
```
The website will then be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)