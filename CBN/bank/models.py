from django.db import models

COURSE_CHOICES=(
    ("Access Bank","Access Bank"),
    ("Fidelity Bank","Fidelity Bank"),
    ("First City Monument Bank","First City Monument Bank"),
    ("Zenith Bank","Zenith Bank"),
    ("Wema Bank","Wema Bank"),
)



class Bank(models.Model):
    name = models.CharField(max_length=255)
    logo = models.TextField(max_length=150)

    def __str__(self):
        return self.name



class Customer(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number =models.BigIntegerField()
    bank = models.CharField(choices= COURSE_CHOICES,max_length=200)
    account_number = models.BigIntegerField()
    date_of_birth = models.DateTimeField() 
    
    
    
    def __str__(self):
        return self.name




