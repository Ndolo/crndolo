from django.db import models

# Create your models here.
class AboutMe(models.Model):
	title = models.CharField(max_length = 255)
	about_me = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title