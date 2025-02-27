from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Blogger
from user.models import User
from .permissions import IsOwnerOrReadOnly
from .serializers import BloggerSerializer, UserSerializer

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope


class BloggerView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, pk=None):
        if pk:
            # FIXME: proper response should be sent if the key does not exist...!!!
            article = Blogger.objects.get(pk=pk)
            serializer = BloggerSerializer(article, many=False)
        else:
            articles = Blogger.objects.all()
            serializer = BloggerSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        article = request.data
        serializer = BloggerSerializer(data=article)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save(author=self.request.user)
            return Response({'Success': 'Article {} created successfully'.format(article_saved.title)},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_article = get_object_or_404(Blogger.objects.all(), pk=pk)
        data = request.data
        serializer = BloggerSerializer(
            instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = get_object_or_404(Blogger.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},
                        status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, TokenHasReadWriteScope)
    queryset = User.objects.all()
    serializer_class = UserSerializer
