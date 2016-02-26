from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.conf import settings


# class ControlPanel(models.Model):

# 	name = models.CharField(max_length=128, unique=True)

# 	def __unicode__(self):
# 		return self.name

# 	def __str__(self):	#for python 3
# 		return self.title



# class Page(models.Model):
# 	#category = models.ForeignKey(Category)
# 	title = models.CharField(max_length=128)
# 	url = models.URLField()
# 	views = models.IntegerField(default=0)

# 	def __unicode__(self):
# 		return self.name

# 	def __str__(self):	#for python 3
# 		return self.title






		


# class Post(models.Model):
# 	picture = forms.CharField(label='search', 
#                     widget=forms.TextInput(attrs={'placeholder': 'Search'}))
# 	chilNo = models.objects.values_list('1', '2','3','4','5','6','7')
# 	bio = models.TextField()
   
# 	name = models.CharField(max_length=120)
# 	gender = models.objects.values_list('male', 'female')
# 	age = models.objects.values_list('1','2','3','4','5','6','7','8','9','10')

#     # child 2
# 	name = models.CharField(max_length=120)
# 	gender = models.objects.values_list('male', 'female')
# 	age = models.objects.values_list('1','2','3','4','5','6','7','8','9','10')

#     # child 3
# 	name = models.CharField(max_length=120)
# 	gender = models.objects.values_list('male', 'female')
# 	age = models.objects.values_list('1','2','3','4','5','6','7','8','9','10')

#     # child 4
# 	name = models.CharField(max_length=120)
# 	gender = models.objects.values_list('male', 'female')
# 	age = models.objects.values_list('1','2','3','4','5','6','7','8','9','10')

#     # child 5
# 	name = models.CharField(max_length=120)
# 	gender = models.objects.values_list('male', 'female')
# 	age = models.objects.values_list('1','2','3','4','5','6','7','8','9','10')

#     # child 6
# 	name = models.CharField(max_length=120)
# 	gender = models.objects.values_list('male', 'female')
# 	age = models.objects.values_list('1','2','3','4','5','6','7','8','9','10')

#     # child 7
# 	name = models.CharField(max_length=120)
# 	gender = models.objects.values_list('male', 'female')
# 	age = models.objects.values_list('1','2','3','4','5','6','7','8','9','10')

# 	number = models.TextField(max_length=120)
    


# 	def __str__(self):
# 		return self.title