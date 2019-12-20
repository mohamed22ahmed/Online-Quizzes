from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    status = models.CharField(max_length=1,default=1)
    user_class = models.CharField(max_length=1)

class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    password = models.CharField(max_length=225,default="123")
    quiz_class = models.CharField(max_length=1)

class Content(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey('Quiz',on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    choos1 = models.CharField(max_length=500)
    choos2 = models.CharField(max_length=500)
    choos3 = models.CharField(max_length=500)
    choos4 = models.CharField(max_length=500)
    correct = models.CharField(max_length=500)

class User_Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    degree = models.CharField(max_length=2)

