from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(db_index=True)
    description = models.TextField()
    
    
    
    def __str__(self):
        return self.title
