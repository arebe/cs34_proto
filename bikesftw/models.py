# encoding: utf-8
import os
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)

@python_2_unicode_compatible
class Bike(models.Model):
	owner = models.ForeignKey('auth.User')
	name = models.CharField(max_length=200)
	#image = ImageField(upload_to=get_image_path, blank=True, null=True)
	frame = models.TextField()
	other = models.TextField()
	date_created = models.DateTimeField('date created')
	date_updated = models.DateTimeField('date updated')

	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = now()
		self.date_updated = now()
		super(Bike, self).save(*args, **kwargs)

	def __str__(self):
		return self.name