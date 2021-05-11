from django.contrib import admin as a
from django.urls import path,include
urlpatterns = [
    path('admin/', a.site.urls),
    path('',include('dogemanager.urls')),
]
