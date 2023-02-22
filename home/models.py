from django.db import models

# Create your models here.

class age_varient(models.Model):
    age_btw = models.CharField(max_length=100)

    def __str__(self):
        return self.age_btw

class gender_varient(models.Model):
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender

class place(models.Model):
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.location

class occupations(models.Model):
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.occupation   
    
class People(models.Model):
    image = models.ImageField(upload_to='statics/people')
    name = models.CharField(max_length=100)
    age = models.ForeignKey(age_varient,blank = True,null = True,on_delete=models.PROTECT)
    gender_type = models.ForeignKey(gender_varient,blank = True,null = True,on_delete=models.PROTECT)
    places = models.ForeignKey(place,blank = True,null = True,on_delete=models.PROTECT)
    occupation_type = models.ForeignKey(occupations,blank = True,null = True,on_delete=models.PROTECT)

    def __str__(self):
        return self.name