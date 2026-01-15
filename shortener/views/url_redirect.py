from django.shortcuts import redirect

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from applibs.logger import get_logger
from shortener.models import UrlShortener
from applibs.helper import generate_hashed_token
from applibs.status import INVALID_LINK_PROVIDED

logger = get_logger(__name__)

class RedirectUrlAPIView(APIView):
    def get(self, request: Request, token: str) -> Response:
        hashed_token = generate_hashed_token(token)
        short_url_object = UrlShortener.objects.fetch_short_url_by_hashed_token(hashed_token)
        if not short_url_object:
            return Response(INVALID_LINK_PROVIDED, status=status.HTTP_400_BAD_REQUEST)
        
        url = short_url_object.url
        logger.info("Saved Url %s", url)
        return redirect(url)