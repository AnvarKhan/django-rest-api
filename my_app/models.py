from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	firstname = models.CharField(max_length=200)
	lastname = models.CharField(max_length=200)
	username = models.CharField(max_length=200, unique=True)
	password = models.CharField(max_length=200)
	createdat = models.DateTimeField(auto_now_add=True)
	updatedat = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.firstname


class Client(models.Model):
	# Prosseccld = models.IntegerField()
	FirstName = models.CharField(max_length=200)
	LastName = models.CharField(max_length=200)
	CarModel = models.CharField(max_length=100)
	CarNumber = models.CharField(max_length=100)
	PhoneNumber = models.CharField(max_length=100)
	CreatedUserld = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
	# UpdatedUserld = models.ForeignKey(User,blank=False,null=True,on_delete=models.SET_NULL)
	CreatedAt = models.DateTimeField(auto_now_add=True)
	UpdatedAt = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.FirstName