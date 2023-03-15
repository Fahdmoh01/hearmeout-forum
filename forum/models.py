from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
	NAME_MAX_LENGTH = 128
	name = models.CharField(max_length = NAME_MAX_LENGTH, unique=True)
	engagements = models.IntegerField(default=0)
	
	#adding a slug field to slugify URLS.
	#always add the unique attribute after following creating your Database and populating it.
	#else there will be migration issues
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
		
	
	# this Meta class allwos for th correct plural of model names in Django admin panel
	class Meta:
			verbose_name_plural = 'Categories'

	#provides a string representation of the Category class
	def __str__(self):
		return self.name
	



class Post(models.Model):
	TOPIC_MAX_LENGTH = 128
	COMMENT_MAX_LENGTH = 250

	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	topic = models.CharField(max_length=TOPIC_MAX_LENGTH)
	comment = models.CharField(max_length=COMMENT_MAX_LENGTH)
	likes= models.IntegerField(default=0)


	class Meta:
		verbose_name_plural = 'Posts'

	def __str__(self):
		return self.topic
	

class UserProfile(models.Model):
	#This line is required to link a UserProfile to a User model instance
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	
	#The additional attributes we wish to include.
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.user.username