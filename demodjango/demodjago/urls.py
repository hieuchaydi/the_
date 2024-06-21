from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),  # Assuming you have a home app
    path('blog/', include('blog.urls')),
     path('contact/', include('contact.urls')),
    
]
