from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class LeadersModel(models.Model):
  id= models.CharField(max_length=20, primary_key=True)
  name=models.CharField(max_length =200)
  phone= PhoneNumberField(unique = True, null = False, blank = False) 
  email  = models.EmailField(max_length=70,blank=True,unique=True)
  description= models.TextField()
  class Meta:
    db_table = "LeadersModel"
  def __str__(self):
        return self.name