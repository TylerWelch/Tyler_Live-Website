from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField('date published')
	blogimage = models.ImageField(default='default.jpg', upload_to='mainsite_pics')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogpost-detail', kwargs= {'pk': self.pk})

class PortfolioPost(models.Model):
	port_title = models.CharField(max_length=200)
	port_description = models.CharField(max_length=200)
	port_date_posted = models.DateTimeField('date published')
	port_content = models.TextField()
	port_image = models.ImageField(default='default.jpg', upload_to='mainsite_pics')

	def __str__(self):
		return self.port_title

	def get_absolute_url(self):
		return reverse('portfoliopost-detail', kwargs= {'pk': self.pk})
