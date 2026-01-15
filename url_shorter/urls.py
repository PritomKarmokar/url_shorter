from django.conf import settings
from django.contrib import admin
from django.urls import path, include

prefix_url = settings.PROJECT_NAME

urlpatterns = [
    path(f'{prefix_url}/admin/', admin.site.urls),
    path('/', include('shortener.urls')),
]

# Admin
admin.site.site_header = "URL Shortener"
admin.site.index_title = "URL Shortener"
admin.site.site_title = "URL Shortener Admin"