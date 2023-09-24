from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True)
    image = models.ImageField(default=None, null=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    subtitle = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)    

    class Meta:
        ordering = ('-updated_at', )
        # verbose_name_plural = "statuses"
        
    def __str__(self):
        return self.title
    
    def snippet(self, arg):
        if len(arg) > 20:
            return arg[:20] + '...'
        return arg
