from django.urls import path

from shortener.views import GenerateShortUrlAPIView, RedirectUrlAPIView

urlpatterns = [
    path(
        'generate-short-url/',
        GenerateShortUrlAPIView.as_view(),
        name='generate-short-url'
    ),
    path(
        '/<str:token>/',
        RedirectUrlAPIView.as_view(),
        name='redirect-url'
    ),
]