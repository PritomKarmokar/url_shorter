from rest_framework import serializers

class URLShortenerSubmitSerializer(serializers.Serializer):
    url = serializers.CharField()