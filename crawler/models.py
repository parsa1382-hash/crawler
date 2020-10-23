from django.db import models


class Sahm(models.Model):
	name = models.CharField(max_length = 500)
	




class Info(models.Model):
    sahm = models.ForeignKey(Sahm, on_delete=models.CASCADE)
    date = models.DateTimeField()
    first = models.IntegerField(default = 0)
    high = models.IntegerField(default = 0)
    low = models.IntegerField(default = 0)
    close = models.IntegerField(default = 0)



# Create your models here.
