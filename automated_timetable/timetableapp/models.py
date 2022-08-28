from django.db import models

# Create your models here.
class courses(models.Model):
	coursename=models.CharField(max_length=100)
	coursecode=models.CharField(max_length=100)
	lecturer = models.CharField(max_length = 200)
	day=models.CharField(max_length=3)
	roomno = models.CharField(max_length = 1000)
	# starttime= models.TimeField()
	# endtime= models.TimeField()

	# renames the instances of the model
	# with their title name
	# def __str__(self):
	# 	return self.title