from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=40)
    email=models.EmailField(default='none')
    subject=models.CharField(max_length=100)
    date=models.DateField()
    message=models.TextField(max_length=1000)

    def __str__(self):
        return self.name
class Projects(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    caption1=models.CharField(max_length=20)
    caption2=models.CharField(max_length=20)
    caption3=models.CharField(max_length=20)
    caption4=models.CharField(max_length=20)
    img1= models.ImageField(upload_to='projects-portfolio')
    img2= models.ImageField(upload_to='projects-portfolio')
    img3= models.ImageField(upload_to='projects-portfolio')
    img4= models.ImageField(upload_to='projects-portfolio')
    link=models.URLField(default="https://www.google.com/")
    def __str__(self):
        return self.name