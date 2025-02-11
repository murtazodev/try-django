from django.db import models
from django.utils.timezone import localtime
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save

class Article(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True, unique=True)
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
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug

            # Ensure uniqueness
            counter = 1
            while Article.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1

        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    # print("Article Pre Save")
    if instance.slug is None:  
        slug = slugify(instance.title)
        instance.slug = slug
    
pre_save.connect(article_pre_save, sender=Article)

def article_post_save(sender, instance, created, *args, **kwargs):
    # print("Article Post Save")
    if created:
        instance.slug = f"{instance.slug}-{instance.id}"
        instance.save()
    
post_save.connect(article_post_save, sender=Article)
