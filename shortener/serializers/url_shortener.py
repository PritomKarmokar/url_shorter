from rest_framework import serializers

class GenerateShortUrlSerializer(serializers.Serializer):
    url = serializers.CharField()