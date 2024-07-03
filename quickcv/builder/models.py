from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class resume(models.Model):
    #basic info on left side of resume
    name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    phone_number = PhoneNumberField(blank=True)
    email=models.EmailField(max_length=100)
    website=models.CharField(max_length=100)
    skill1=models.CharField(max_length=100)
    skill2=models.CharField(max_length=100)
    skill3=models.CharField(max_length=100)
    skill4=models.CharField(max_length=100)
    skill5=models.CharField(max_length=100)
    twitter=models.CharField(max_length=100)
    ytb=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)
    lang1=models.CharField(max_length=100)
    lang2=models.CharField(max_length=100)
    #right side of resume
    about=models.TextField()
    #work experience
    work1=models.CharField(max_length=100)
    work1_info=models.TextField(max_length=200)
    work2=models.CharField(max_length=100)
    work2_info=models.TextField(max_length=200)
    #projects
    project1=models.CharField(max_length=100)
    project1_info=models.TextField(max_length=200)
    project2=models.CharField(max_length=100)
    project2_info=models.TextField(max_length=200)
    project3=models.CharField(max_length=100)
    project3_info=models.TextField(max_length=200)
    #education
    collegeName=models.CharField(max_length=100)
    college_course=models.TextField(max_length=200)
    schoolName=models.CharField(max_length=100)
    school_info=models.TextField(max_length=200)
    #certification
    certificate1=models.CharField(max_length=100)
    certificate1_info=models.TextField(max_length=200)
    certificate2=models.CharField(max_length=100)
    certificate2_info=models.TextField(max_length=200)

    def __str__(self):
        return self.name