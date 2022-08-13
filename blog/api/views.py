from urllib import request
from blog.api import serializers
import django_filters
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)

from django.http import Http404
from blog.models import Blog
from blog.api.serializers import BlogCreateSerializer, BlogReadSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class  CustomListCreateAPIView(ListCreateAPIView):
    queryset=Blog.objects.all()
    def get_serializer_class(self):
        # return self.serializer_classes.get(self.request.method)
        if self.request.method== 'GET':
            return BlogReadSerializer
        return  BlogCreateSerializer
        

        


class BlogListCreateAPI(CustomListCreateAPIView,django_filters.FilterSet):
    queryset= Blog.objects.all()
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend,  filters.OrderingFilter)
    filter_fields = ('category', 'tags')
    serializer_classes = {
        'GET': BlogReadSerializer,
        'POST': BlogCreateSerializer
    }
    parser_classes = [FormParser, MultiPartParser]
    # serializer_class = BlogCreateSerializer

class BlogRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Blog.objects.all()
    serializer_class = BlogCreateSerializer
    parser_classes = [FormParser, MultiPartParser]




