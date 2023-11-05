from django.db import models
from django.contrib.auth.models import User  # Assuming you're using the built-in User model

# Create your models here.
class TextEntry(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.text  # This is a string representation of the model instance


class JobPost(models.Model):
    company_id = models.IntegerField()
    job_title = models.CharField(max_length=100)  # New field for job title
    job_description = models.CharField(max_length=300)
    posted_date = models.DateField()
    location = models.CharField(max_length=100)
    vacancy = models.PositiveIntegerField()
    job_nature = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    application_date = models.DateField()
    skills_req = models.CharField(max_length=300)
    experience = models.PositiveIntegerField()
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title


class CompanyDetails(models.Model):
    company_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    company_name = models.CharField(max_length=100)
    company_ceo_name = models.CharField(max_length=100)
    company_mail = models.EmailField()
    company_site = models.URLField()
    company_description = models.TextField(null=True, blank=True)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    company_linkedin = models.URLField(null=True, blank=True)
    company_location = models.CharField(max_length=100, null=True, blank=True)
    starting_year = models.DateField()
    employees = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.company_name
    
class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    mailid = models.EmailField()
    linkedin = models.URLField(blank=True)
    githublink = models.URLField(blank=True)
    skills = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    dateofbirth = models.DateField()
    about = models.TextField(blank=True)
    phone_no = models.CharField(max_length=15, blank=True)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name
    