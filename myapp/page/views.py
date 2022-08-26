from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from page.models import Page, Post, Tag
from page.serializer import PageSerializer, PostSerializer, TagSerializer
from rest_framework import mixins, viewsets
from services.page_service import PageService, PostService


class PageViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class TagViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@login_required
def main_page(request):
    return PageService().main_page(request)


@login_required
@csrf_exempt
def create_post(request):
    return PostService().create_post(request)
