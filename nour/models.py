from django.db import models



def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "homes/%s.%s"%(instance,extension)

# Create your models here.
class Servies(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to=image_upload)


    def __str__(self):
        return self.name


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to=image_upload)
    specialization = models.CharField(max_length = 100)

    def __str__(self):
        return self.name        
    


class Product(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to=image_upload)
    
    def __str__(self):
        return self.name      
    



class Price_left(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to=image_upload)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()    
    def __str__(self):
        return self.name       
    


class Price_right(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to=image_upload)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()    
    def __str__(self):
        return self.name       
    

class Gallery(models.Model):
    image = models.ImageField(upload_to=image_upload)
 


class Nails(models.Model):
    image = models.ImageField(upload_to=image_upload)
  
class Eye(models.Model):
    image = models.ImageField(upload_to=image_upload)

class Lips(models.Model):
    image = models.ImageField(upload_to=image_upload)



class Eyebrows(models.Model):
    image = models.ImageField(upload_to=image_upload)


class Dress(models.Model):
    image = models.ImageField(upload_to=image_upload)