from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ShortenedURL
from .serializers import ShortenedURLSerializer
import string
import random

def generate_short_key():
    # Generate a random 6-character short key
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

class ShortenURLView(generics.CreateAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer

    def create(self, request, *args, **kwargs):
        # Generate a unique short key
        short_key = generate_short_key()

        # Ensure the short key is unique
        while ShortenedURL.objects.filter(short_key=short_key).exists():
            short_key = generate_short_key()

        # Create the ShortenedURL instance
        request.data['short_key'] = short_key
        return super().create(request, *args, **kwargs)

class RedirectURLView(generics.RetrieveAPIView):
    queryset = ShortenedURL.objects.all()
    serializer_class = ShortenedURLSerializer
    lookup_field = 'short_key'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Redirect to the long URL
        return Response(status=status.HTTP_302_FOUND, headers={'Location': instance.long_url})
