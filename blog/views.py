from blog.models import Post
from blog.serializer import PostSerializer

from blog.pagination import Mypagination
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    pagination_class = Mypagination
