from rest_framework import generics

from .models import Blogger
from .serializers import BloggerSerializer

class BloggerList(generics.ListAPIView):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer


class BlogDetail(generics.RetrieveAPIView):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer
