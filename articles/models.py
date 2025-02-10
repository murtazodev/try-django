from django.db import models
from django.utils.timezone import localtime

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def created_at_kst(self):
        return localtime(self.created_at)
    
    def updated_at_kst(self):
        return localtime(self.updated_at)
    
    def __str__(self):
        return f"{self.id} - {self.title}"
