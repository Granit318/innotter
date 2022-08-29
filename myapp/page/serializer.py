from page.models import Page, Post, Tag
from rest_framework import serializers


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = (
            "name",
            "uuid",
            "description",
            "tags",
            "owner",
            "followers",
            "image",
            "is_private",
            "follow_requests",
            "unblock_date",
        )


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "page",
            "content",
            "reply_to",
            # 'created_up',
            # 'updated_at',
        ]
