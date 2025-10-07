from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # we won't use admin for CRUD, but leaving it doesn't hurt
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),  # send root to our app
]
