from django.urls import path
from .views import PostRetrieveUpdateDestroyAPIView, PostListCreateAPIView


app_name = 'post'


urlpatterns = [
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path('', PostListCreateAPIView.as_view(), name='list'),
]



