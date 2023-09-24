from rest_framework import serializers

from ..models import Newsletter


class NewsletterSerializer(serializers.ModelSerializer):

    # review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Newsletter
        # exclude = ("ebook",)
        fields = "__all__"
