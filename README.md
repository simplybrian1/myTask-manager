FOLLOW THE STEPS AS IS TO RUN  THE SERVER

git clone https://github.com/simplybrian1/myTask-manager.git


cd myTask-manager


python -m venv venv


venv\Scripts\activate


cd task_manager

pip install -r requirements.txt


pip install pymysql

cd ..

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver


FOR DATABASE 
you'll need to download mysql

CREATE DATABASE taskdb;

open task_manager/settings.py and update this section to 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taskdb',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Replace 'your_mysql_user' and 'your_mysql_password' with their actual MySQL username and password.


