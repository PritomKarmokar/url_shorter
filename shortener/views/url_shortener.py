from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from applibs.logger import get_logger
from shortener.models import UrlShortener
from applibs.status import VALID_DATA_NOT_FOUND
from shortener.serializers import URLShortenerSubmitSerializer

logger = get_logger(__name__)

class URLShortenerSubmitAPIView(APIView):
    serializer_class = URLShortenerSubmitSerializer

    def post(self, request: Request) -> Response:
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            logger.error("Invalid serializer data: %s ", serializer.errors)
            return Response(data=VALID_DATA_NOT_FOUND, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        url = validated_data.get("url")

        url_object = UrlShortener.objects.create_short_url(url)
        if not url_object:
            logger.error("Error Creating new short url object")
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)