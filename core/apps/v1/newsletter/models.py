from django.db import models
from django.contrib.auth.models import User

class Newsletter(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(max_length=255, null=False, blank=False)
    attachment = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ('-updated_at', )

    def __str__(self):
        return self.title
    
    def snippet(self, arg):
        if len(arg) > 20:
            return arg[:20] + '...'
        return arg


# class Subscriber(models.Model):
#     email = models.EmailField(unique=True, null=False, blank=False)
#     token = models.UUIDField(default=uuid4, unique=True)
#     canceled = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, editable=False)
#     updated = models.DateTimeField(auto_now=True)    
    
#     def __str__(self):
#         return self.email