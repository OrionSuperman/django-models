from __future__ import unicode_literals
from datetime import datetime, time
from django.db import models

class Interest(models.Model):
	name = models.TextField(max_length=100)
	created_at = models.DateTimeField(default = datetime.now().strftime("%Y-%m-%d"))
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'interests'

class User(models.Model):
	now = datetime.now()
	first_name = models.TextField(max_length=100)
	last_name = models.TextField(max_length=100)
	age = models.IntegerField()
	created_at = models.DateTimeField(default = datetime.now().strftime("%Y-%m-%d"))
	occupation = models.TextField(max_length=100)
	interest = models.ForeignKey(Interest)
	def __str__(self):
		return self.first_name
	class Meta:
		db_table = 'users'
