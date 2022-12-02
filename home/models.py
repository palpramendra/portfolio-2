from django.db import models

# Create your models here.
class Feedback(models.Model):

    name = models.CharField(max_length=408)
    post = models.CharField(max_length=500)
    comment = models.TextField()
    image = models.TextField()


    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=500,blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name


