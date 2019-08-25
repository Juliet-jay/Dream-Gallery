from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.

class CategoryTestClass(TestCase):
    def setUp(self):
        self.nature = Category(name = 'nature')
    def test_instance(self):
        self.assertTrue(isinstance(self.nature, Category))
    def test_save_method(self):
        self.nature.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    def test_delete_method(self):
        self.new_category = Category(name = 'spring')
        self.new_category.save_category()
        self.new_category.delete_category()
        categories = Category.objects.all()
        self.assertEqual(len(categories), 0)   
    def test_update_category(self):
        self.health = Category(name = 'motobikes')
        self.health.save_category()
        self.health = Category(name = 'cars')
        self.health.save_category()
        self.health.update_category(name = 'Nature')
        categories = Category.objects.filter(name = 'People')
        self.assertEqual(len(categories), 1)

class LocationTestClass(TestCase):    
    def setUp(self):
        self.Kenya = Location(name = 'Kenya')
    def test_instance(self):
        self.assertTrue(isinstance(self.Kenya, Location))
    def test_save_method(self):
        self.Kenya.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    def test_delete_method(self):
        self.new_location = Location(name = 'Mombasa')
        self.new_location.save_location()
        self.new_location.delete_location()
        locations = Location.objects.all()
        self.assertEqual(len(locations), 0)
    def test_update_method(self):
        self.Nairobi = Location(name = 'Mombasa')
        self.Nairobi.save_location()
        self.Nairobi = Location(name = 'Nairobi')
        self.Nairobi.save_location()
        self.Nairobi.update_location(name = 'Nairobi')
        locations = Location.objects.filter(name = 'Nairobi')
        self.assertEqual(len(locations), 1)  
        
 class ImageTestClass(TestCase):
    
    def setUp(self):
        self.school = Image(name = 'school', description = 'school character')
        self.school.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.school, Image))
    def test_save_method(self):
        self.school.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0) 
    def test_delete_method(self):
        self.new_image = Image(name = 'flower', description = 'the attractive scent of the flower despite the thorns')  
        self.new_image.save_image() 
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertEqual(len(images), 1)
    def test_update_method(self):
        self.jules = Image(name = 'jules', description = 'picture of jules')
        self.jules.save_image()
        self.jules = Image(name = 'jules', description = 'picture of jules')        
        self.jules.update_image(name = 'jules')
        self.jules.save_image()
        images = Image.objects.filter(name = 'jules')
        pics = Image.objects.all()      
        self.assertEqual(len(images), 1)
        