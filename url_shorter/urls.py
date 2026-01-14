from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('shortener.urls')),
]

# Admin
admin.site.site_header = "URL Shortener"
admin.site.index_title = "URL Shortener"
admin.site.site_title = "URL Shortener Admin"