from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="cover_pictures", verbose_name="Cover Image")
    likes = models.ManyToManyField(User, related_name="posts_liked")

    def __str__(self):
        return f"{self.title, self.id}"

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"pk": self.pk})