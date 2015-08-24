image fields require Pillow library 
http://pillow.readthedocs.org/en/latest/

to install it on ubuntu you need to intall python-dev it also requires pip install

after deploying you need to manage.py collectstatic command
and restart apache in order to fix admin statics

also set static and media root directly

live'da makemigrations yemedi syncdb yaptým

django-tinymce required get it pip install django-tinymce add apps and copy its statics to ur static folder
for model change html field

django-recaptcha required for recaptcha get it by pip install django-recaptcha and add adpps