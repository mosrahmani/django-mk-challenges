from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body', 'created', 'owner']
        read_only_fields = ['owner']


class PostDetailSerializer(serializers.ModelSerializer):
    comment_set = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment_detail'
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'created', 'updated', 'owner', 'comment_set']
        read_only_fields = ['owner']


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='post_detail',
    )

    class Meta:
        model = Comment
        fields = ['post', 'owner', 'body', 'created', 'updated']
        read_only_fields = ['owner']
