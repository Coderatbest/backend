# django backend coderatbest.com
```
$ pip install django
```
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

## add maria db
### add to requirements.txt
- dj-database-url==0.5.0
- environ==1.0
- mysqlclient 2.0.3

### envs 
more information https://github.com/jacobian/dj-database-url
- db_pass=password
- DB_URL=mysql://USER:PASSWORD@HOST:PORT/NAME

note: change the values

```bash
#create .env
echo "DB_ROOT_PASSWORD=root_password
DB_PASSWORD=password
DB_USER=$USER
DB_HOST=db
DB_NAME=coderatbest
DB_PORT=3306
" > .env

```

### migrations

```
docker-compose run api python manage.py makemigrations
```
