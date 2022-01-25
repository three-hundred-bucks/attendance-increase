@echo off
python manage.py migrate
pause
py manage.py runserver 0.0.0.0:8000 
pause