from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=100)
	is_password = models.BooleanField(default=False)
	uid = models.IntegerField()
	gid = models.IntegerField()
	fullname = models.CharField(max_length=100)
	home = models.CharField(max_length=100)
	shell = models.CharField(max_length=100)

	
	def __str__(self):
		return "{} ({}-{})".format(self.username, self.uid, self.gid)