from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$',views.gallery,name = 'gallery'),
    url(r'^categories/',views.display_images_categories,name = 'categories'),
    url(r'^locations/',views.display_images_locations,name= 'locations'),
    url(r'^search/',views.search_results,name = 'search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)