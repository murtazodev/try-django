from django.db import models
from django.utils.timezone import localtime
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def created_at_kst(self):
        return localtime(self.created_at)
    
    def updated_at_kst(self):
        return localtime(self.updated_at)
    
    def __str__(self):
        return f"{self.id} - {self.title}"
    
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
