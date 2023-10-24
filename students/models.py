from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    middlename = models.CharField(max_length=150,default='null')
    birthday = models.DateField(blank=True, null=True)
    nic = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=60,default='null')
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10,default='male')
    student_img = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True ,default='photos/1.jpg')
    address = models.CharField(max_length=100,blank=True, null=True)
    town = models.CharField(max_length=20,blank=True, null=True)
    email = models.CharField(max_length=30,blank=True, null=True)
    mobileno1 = models.IntegerField(blank=True, null=True)
    mobileno2 = models.IntegerField(blank=True, null=True)



    def __str__(self):
        return self.name
        # return self.nic
