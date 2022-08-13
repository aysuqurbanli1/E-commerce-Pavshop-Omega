from rest_framework import serializers
# from drf_yasg.utils import swagger_serializer_method
from blog.models import Blog,Comment,Category
from core.models import Tag
from account.api.serializers import *
from product.api.serializers import *
from drf_yasg.utils import swagger_serializer_method


User = get_user_model()


class BlogCreateSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = (
            'category', 
            'author',
            'tags',
            'title',
            'slug',
            'description',
            'image',
            'comment',
        )

    # @swagger_serializer_method()  
    def get_image(self, obj):
        images = obj.image.all().values_list("image")
        img_list = []
        for img in images:
            img_list.append(
                {   
                    'image':img[0],
                }
            )
        return img_list



    def get_comment(self, obj):
        comments = obj.blogcomment.all().values_list("review", 'reply')
        comments_list = []
        for i in comments:
            comments_list.append(
                {
                    'review':i[0],
                    'reply':i[1]
                }
            )
        return comments_list


class BlogReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    author = UserSerializer()
    comment = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'category', 
            'author',
            'tags',
            'title',
            'slug',
            'description',
            'image',
            'comment',
        )

    # @swagger_serializer_method()
    def get_comment(self, obj):
        comments = obj.blogcomment.all().values_list("review", 'reply')
        comments_list = []
        for i in comments:
            comments_list.append(
                {
                    'review':i[0],
                    'reply':i[1]
                }
            )
        return comments_list
 

class ReviewSerializer(serializers.ModelSerializer):
    user = str(UserSerializer())

    class Meta:
        model = Comment
        fields = (
            'user',
            'blog',
            'review',
            'reply',
        )