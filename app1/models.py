from django.db import models

# Create your models here.
class Dept(models.Model):
    sno=models.CharField(max_length=100,primary_key=True)
    subject=models.CharField(max_length=100)
    gmail=models.EmailField()

    def __str__(self):
        return self.sno
class Student(models.Model):
    sno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    sname=models.CharField(max_length=100)
    number=models.IntegerField()
    standard=models.CharField(max_length=100)

    def __str__(self):
        return self.sname
class Fees(models.Model):
    sname=models.ForeignKey(Student,on_delete=models.CASCADE)
    amount=models.IntegerField()
    
    def __str__(self):
        return str(self.amount)