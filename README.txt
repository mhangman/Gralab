GRALAB

Flash game portal with Django

1-image fields require Pillow library 
http://pillow.readthedocs.org/en/latest/

to install it on ubuntu you need to intall python-dev it also requires pip install

2-after deploying you need to manage.py collectstatic command
and restart apache in order to fix admin statics

also set static and media root directly

3-at live makemigrations can cause problem try syncdb if it fails

4-django-tinymce required, get it with "pip install django-tinymce", add apps and copy its statics to your static folder
for model change html field

5-django-recaptcha required for recaptcha get it by pip install django-recaptcha and add apps