from django.db import models

# Create your models here.

#creating the company model:
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT','IT'), 
                                                     ('Non IT', 'Non IT'), 
                                                     ('Analyst', 'Analyst')
                                                     )
                            )
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name + ',' + self.location
    
#creating employee model:

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    address = models.CharField(max_length=100)
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    job_positiobn = models.CharField(max_length=50, choices=(('Frontend Developer', 'Frontend Developer'),
                                                             ('Backend Developer', 'Backend Developer'),
                                                             ('Data analyst', 'Data analyst')
                                                             )
                                     )
    
    company = models.ForeignKey(Company,on_delete= models.CASCADE )
    