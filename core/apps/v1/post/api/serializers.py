from rest_framework import serializers

from ..models import Post


class PostSerializer(serializers.ModelSerializer):

    # review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        # exclude = ("ebook",)
        fields = "__all__"
        read_only_fields = ['author']
