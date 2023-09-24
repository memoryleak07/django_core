from django.urls import path
from .views import NewsletterDetail, NewsletterList


app_name = 'newsletter'


urlpatterns = [
    path('<int:pk>/', NewsletterDetail.as_view(), name='detail'),
    path('', NewsletterList.as_view(), name='list'),
]



