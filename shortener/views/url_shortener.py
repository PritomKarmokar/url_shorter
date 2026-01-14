from django.conf import settings

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from applibs.logger import get_logger
from shortener.models import UrlShortener
from applibs.status import (
    VALID_DATA_NOT_FOUND,
    FAILED_TO_GENERATE_SHORT_URL,
    SHORT_URL_GENERATE_SUCCESSFUL
)
from shortener.serializers import GenerateShortUrlSerializer
from applibs.helper import (
    format_output_success,
    generate_hashed_token,
    generate_unique_token_for_url,
)

logger = get_logger(__name__)

class GenerateShortUrlAPIView(APIView):
    serializer_class = GenerateShortUrlSerializer

    def post(self, request: Request) -> Response:
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            logger.error("Invalid serializer data: %s", serializer.errors)
            return Response(
                VALID_DATA_NOT_FOUND,
                status=status.HTTP_400_BAD_REQUEST
            )

        validated_data = serializer.validated_data
        url = validated_data.get("url")

        unique_token = generate_unique_token_for_url()
        hashed_token = generate_hashed_token(unique_token)
        
        url_object = UrlShortener.objects.create_short_url(url, hashed_token)
        if not url_object:
            logger.error("Error Creating new short url object")
            return Response(
                FAILED_TO_GENERATE_SHORT_URL,
                status=status.HTTP_400_BAD_REQUEST
            )

        base_url = settings.URL_SHORTER_BASE_URL
        short_url = f"{base_url}/{unique_token}"
        response_data = {
            "short_url": short_url
        }
        return Response(
            format_output_success(SHORT_URL_GENERATE_SUCCESSFUL, data=response_data),
            status=status.HTTP_201_CREATED
        )