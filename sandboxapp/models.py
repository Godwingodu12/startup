from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Investors(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    document = models.FileField(upload_to="docs")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Startupfounder(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    document = models.FileField(upload_to="docs")
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Idea(models.Model):
    idea = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    desc = models.CharField(max_length=200)
    user = models.ForeignKey(Startupfounder, on_delete=models.CASCADE)


class Comments(models.Model):
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey(Startupfounder, on_delete=models.CASCADE)


class Feedback(models.Model):
    date = models.DateField(auto_now_add=True)
    feedback = models.CharField(max_length=200)
    user = models.ForeignKey(Startupfounder, on_delete=models.CASCADE)


class Chat(models.Model):
    date = models.DateField(auto_now_add=True)
    sender = models.EmailField()
    receiver = models.EmailField()
    message = models.CharField(max_length=200)
    status=models.CharField(max_length=100,default="Delivered")


class Investmentinterest(models.Model):
    date = models.DateField(auto_now_add=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investors, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)


class Payment(models.Model):
    date = models.DateField(auto_now_add=True)
    statup = models.ForeignKey(Startupfounder, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investors, on_delete=models.CASCADE)
    amount = models.CharField(max_length=20)


class WorkSpace(models.Model):
    location = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to="land_images")
    status = models.CharField(default="Free", max_length=100)
    sfid=models.ForeignKey(Startupfounder,on_delete=models.CASCADE,null=True,blank=True)