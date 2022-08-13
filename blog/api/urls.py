from django.urls import path
from blog.api.views import BlogListCreateAPI,BlogRetrieveUpdateDestroyAPIView



urlpatterns = [
    path('blogs/', BlogListCreateAPI.as_view(),  name='api_blogs'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyAPIView.as_view(),),
   
]



