from pydoc import describe
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class activity(models.Model):
    activity_id = models.CharField(max_length=90,primary_key=True)
    activity_name= models.CharField(max_length=30)
    description = models.CharField(max_length=90)
    photo= models.ImageField()
    rate = models.IntegerField()
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "activity"

class idgen1(models.Model):
    activity_id=models.IntegerField()
    resort_id=models.IntegerField()
    homestay_id=models.IntegerField()
    traveller_id=models.IntegerField()
    homestaybooking_id=models.IntegerField()
    resortbooking_id=models.IntegerField()
    activitybooking_id=models.IntegerField()
    act_review_id=models.IntegerField()
    res_review_id=models.IntegerField()
    hom_review_id=models.IntegerField()

   

     
    class Meta:
       db_table = "idgen1" 

class resort(models.Model):
    resort_id = models.CharField(max_length=90,primary_key=True)
    resort_name= models.CharField(max_length=30)
    location = models.CharField(max_length=90)
    photo= models.ImageField()
    description = models.CharField(max_length=90)
    owner=models.CharField(max_length=90)
    contact = models.CharField(max_length=90)
    rate = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "resort"
class homestay(models.Model):
    homestay_id = models.CharField(max_length=90,primary_key=True)
    photo= models.ImageField()
    house_name= models.CharField(max_length=30)
    roof= models.CharField(max_length=90)
    description = models.CharField(max_length=90)
    food=models.CharField(max_length=90)
    owner=models.CharField(max_length=90)
    contact =models.CharField(max_length=90)
    rate = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "homestay"   
class login(models.Model):
    username = models.CharField(max_length=90,primary_key=True)
    password = models.CharField(max_length=30)
    category = models.CharField(max_length=90)
    
    
    class Meta:
        db_table = "login"    
class traveller(models.Model):
    traveller_id = models.CharField(max_length=90,primary_key=True)
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    district = models.CharField(max_length=90)
    country= models.CharField(max_length=30)
    state= models.CharField(max_length=30)
    photo = models.ImageField()
    contact = models.IntegerField()
    email = models.CharField(max_length=90)
    
    class Meta:
        db_table = "traveller" 
                       
class homestaybooking1(models.Model):
    homestaybooking_id = models.CharField(max_length=90,primary_key=True)
    homestay_id= models.ForeignKey(homestay,on_delete=models.CASCADE)
    traveller_id= models.ForeignKey(traveller,on_delete=models.CASCADE)
    booking_date = models.CharField(max_length=90)
    no_of_days= models.CharField(max_length=30)
    no_of_person= models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    
    class Meta:
        db_table = "homestaybooking1" 
                       
class resortbooking1(models.Model):
    resortbooking_id = models.CharField(max_length=90,primary_key=True)
    resort_id= models.ForeignKey(resort,on_delete=models.CASCADE)
    traveller_id= models.ForeignKey(traveller,on_delete=models.CASCADE)
    booking_date = models.CharField(max_length=90)
    no_of_days= models.CharField(max_length=30)
    no_of_person= models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    
    class Meta:
        db_table = "resortbooking1"  

class activitybooking1(models.Model):
    activitybooking_id = models.CharField(max_length=90,primary_key=True)
    activity_id= models.ForeignKey(activity,on_delete=models.CASCADE)
    traveller_id= models.ForeignKey(traveller,on_delete=models.CASCADE)
    booking_date = models.CharField(max_length=90)
    no_of_days= models.CharField(max_length=30)
    no_of_person= models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    
    
    class Meta:
        db_table = "activitybooking1"  

class activityreview(models.Model):
    act_review_id = models.CharField(max_length=90,primary_key=True)
    review = models.CharField(max_length=150)
    review_date = models.CharField(max_length=90)
    traveller_id= models.ForeignKey(traveller,on_delete=models.CASCADE)
    activity_id= models.ForeignKey(activity,on_delete=models.CASCADE)
   
    
    class Meta:
        db_table = "activityreview" 
class resortreview(models.Model):
    res_review_id = models.CharField(max_length=90,primary_key=True)
    review = models.CharField(max_length=150)
    review_date = models.CharField(max_length=90)
    traveller_id= models.ForeignKey(traveller,on_delete=models.CASCADE)
    resort_id= models.ForeignKey(resort,on_delete=models.CASCADE)
   
    
    class Meta:
        db_table = "resortreview"
class homestayreview(models.Model):
    hom_review_id = models.CharField(max_length=90,primary_key=True)
    review = models.CharField(max_length=150)
    review_date = models.CharField(max_length=90)
    traveller_id= models.ForeignKey(traveller,on_delete=models.CASCADE)
    homestay_id= models.ForeignKey(homestay,on_delete=models.CASCADE)
   
    
    class Meta:
        db_table = "homestayreview"                                           
                                                
                      

