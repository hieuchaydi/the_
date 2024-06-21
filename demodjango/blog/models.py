from django.db import models
class postForm(models.Model):
    title=models.CharField(max_length=255)
    body= models.TextField()
    create_at= models.DateTimeField(auto_now_add=True)
# Create your models here.
    def __str__(self):
       return self.title
   