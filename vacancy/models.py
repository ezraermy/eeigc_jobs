from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employer(models.Model):

    catagory = (
        ('Permanent', 'Permanent'),
        ('Contract', 'Contract'),
    )
    name=models.CharField(max_length=200,null=True)
    position=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=2000,null=True)
    experience=models.IntegerField(null=True)
    salary=models.IntegerField(null=True)
    location=models.CharField(max_length=2000,null=True)
    JobType = models.CharField(max_length=200,null=True, choices=catagory)
    DatePublished = models.DateTimeField(null=True)
    deadline = models.DateTimeField(null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Employer'
    
class Employee(models.Model):

    sex = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    name = models.CharField(max_length=200,null=True)
    dob = models.DateTimeField(null=True)
    gender = models.CharField(max_length=20, null=True, choices=sex)
    address = models.CharField(max_length=200, null=True)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=200, null=True)
    CoverLetter = models.FileField(verbose_name='Cover Letter', null=True)
    resume = models.FileField(verbose_name='CV', null=True)
    phd = models.FileField(null=True)
    msc = models.FileField(null=True)
    bsc = models.FileField(null=True)
    od = models.FileField(null=True)
    employer = models.ManyToManyField(Employer, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Employee'
        
