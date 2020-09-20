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
    country = models.CharField(max_length=50)

    birthdate = models.DateField()
    status = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    height = models.CharField(max_length=20)
    weigth = models.CharField(max_length=20)
    religion = models.CharField(max_length=20)

    sp_name = models.CharField(max_length=50)
    sp_job = models.CharField(max_length=50)
    children = models.CharField(max_length=50)
    m_name = models.CharField(max_length=50)
    m_job = models.CharField(max_length=50)
    f_name = models.CharField(max_length=50)
    f_job = models.CharField(max_length=50)

    
    
    class Meta:
        db_table = "Person"

class Customer(Person):
    emp_id = models.AutoField(primary_key=True)
    date_regis = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "Customer"