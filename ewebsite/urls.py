from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from products.views import review_text, add_brand
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),  
    path('', include('cart.urls')),    
    path('', include('order.urls')),
    path('admin/', admin.site.urls),
    path('review/', review_text, name='review'),
    path('add_brand/', add_brand, name='add_brand')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
