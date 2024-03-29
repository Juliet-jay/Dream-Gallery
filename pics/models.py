from django.db import models
import datetime as dt 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    def save_category(self):
        self.save()
    def delete_category(self):
        Category.objects.filter(id = self.pk).delete()
    def update_category(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
        
class Location(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    def delete_location(self,**kwargs):
        self.objects.filter(id = self.pk).delete(**kwargs)
        
    def update_location(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
        
        
class Image(models.Model):
    image = models.ImageField(upload_to = 'pics/',null =True)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category',on_delete =models.CASCADE,null='True',blank=True)
    location =models.ForeignKey('Location',on_delete= models.CASCADE,null='True',blank=True)
    pub_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        image.objects.filter(id =self.pk).delete()
        
    def update_image(self,**kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)
        
        
    @classmethod
    def all_pics(cls):
        pics = cls.objects.all()
        return pics 
    
    @classmethod
    def pic_locations(cls):
        pics = cls.objects.order_by('location')
        return pics 
    
    @classmethod
    def pic_categories(cls):
        pics = cls.objects.order_by('category')
        return pics
    
    @classmethod
    def get_pic(cls, id):
        pic = cls.objects.get(id=id)
        return pic 
    
    @classmethod
    def search_by_category(cls, search_input):
        images = cls.objects.filter(category__name__icontains=search_input)
        return images

