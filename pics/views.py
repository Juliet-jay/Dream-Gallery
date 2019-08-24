from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def index(request):
    images = Image.get_all_images()
    locations = Location.get_locations()
    categories = Category.get_all_categories()
    return render(request,'index.html',{'images':images, 'categories':categories, 'locations':locations})



