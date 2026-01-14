from django.urls import path

from shortener.views import GenerateShortUrlAPIView

url_patterns = [
    path('generate-short-url/', GenerateShortUrlAPIView.as_view(), name='generate-short-url'),
]