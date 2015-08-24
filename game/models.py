from django.db import models
from tinymce import  models as tinymce_models
from django_boto.s3.storage import S3Storage

s3 = S3Storage()

class Genre(models.Model):
	name = models.CharField(max_length="30")
	genre_content = tinymce_models.HTMLField(blank=True)
	
	def __unicode__(self):
		return unicode(self.name)


class Game(models.Model):
	name = models.CharField(max_length="30")
	slug = models.SlugField(max_length="35")
	logo = models.ImageField(blank=True, upload_to='game-logos/', storage=s3)
	source = models.FileField(blank=True, upload_to='game-source/', storage=s3)
	description = tinymce_models.HTMLField(blank=True)
	genre = models.ManyToManyField(Genre)
	publish_date = models.DateField()
	status = models.BooleanField("Active", default=False)
	is_editor = models.BooleanField("Editor's Choice", default=False)
	is_special = models.BooleanField("Special", default=False)

	def __unicode__(self):
		return unicode(self.name)