from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default_profile.jpg", upload_to="profile_pictures", verbose_name="Profile Picture")
    introduction = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

    def save(self, *args, **kwargs):
        self.introduction = f"Hello everybody, my name is {self.user.username}, nice to meet you:D"
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)
