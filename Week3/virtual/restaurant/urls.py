from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('menu/', include('menu.urls')),
    path('souvenirs/', include('souvenirs.urls')),
    path('attractions/', include('attractions.urls')),
    path('discounts/', include('discounts.urls')),
]
