from django.db import models


# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=128, help_text="Name: ")
    phone = models.IntegerField(help_text="Phone Number: ")
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField
    address = models.CharField(max_length=200, help_text="Address: ")
    photo = models.ImageField(help_text="Upload image: ")
    description = models.CharField(max_length=500, help_text="Comments: ")

    def save(self, *args, **kwargs):
        super(Agent, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
