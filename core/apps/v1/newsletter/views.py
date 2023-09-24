# from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics

from .models import Newsletter

from .api.serializers import NewsletterSerializer
from .api.pagination import SmallSetPagination


class NewsletterList(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAdminUser]
    pagination_class = SmallSetPagination

class NewsletterDetail(generics.RetrieveDestroyAPIView): # with DEL or RetrieveAPIView
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    permission_classes = [IsAdminUser]