# django backend coderatbest.compip install django

## create setup

```
django-admin startproject mysite || sudo apt install python3-django

pip install djangorestframework

python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin

python3  manage.py startapp users
python3  manage.py startapp utilies

```
## Add custom model user

- edit file settings.py
- add varible AUTH_USER_MODEL='users.User'