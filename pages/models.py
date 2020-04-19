from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_image')
    

    def __str__(self):
        return self.title