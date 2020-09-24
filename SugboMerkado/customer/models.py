from django.db import models

# Create your models here.
class Person(models.Model):
    profile_pic = models.ImageField(default = "placeholder.png") 

    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    brgy = models.CharField(max_length=50)
    prov = models.CharField(max_length=50)
    zp = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default= "Philippines")

    birthdate = models.DateField()
    status = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    religion = models.CharField(max_length=20)

    sp_name = models.CharField(max_length=50)
    sp_job = models.CharField(max_length=50)
    children = models.IntegerField(default = 0)
    m_name = models.CharField(max_length=50)
    m_job = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    f_job = models.CharField(max_length=50)

    email = models.EmailField(max_length=50, blank = True)
    phone = models.CharField(max_length=11, blank = True)
    
    class Meta:
        db_table = "Person"

class Customer(Person):
    emp_id = models.AutoField(primary_key=True)
    date_regis = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Customer"
