from django.db import models


class message(models.Model):
	user = models.CharField( max_length = 100);
	title = models.CharField(max_length = 300)
	description = models.CharField(max_length = 10000)
	pub_date = models.DateTimeField( blank = True, null = True)

	def __str__(self):
		return self.title


# Create your models here.
