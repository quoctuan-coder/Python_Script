from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(default='profile_pics/profile-pic-default.png', upload_to='profile_pics', blank=True)
    address = models.CharField(max_length=100, help_text='Enter Your Address', null=True, blank=True)
    city = models.CharField(max_length=100, help_text='Enter Your City', null=True, blank=True)
    country = models.CharField(max_length=100, help_text='Enter Your Country', null=True, blank=True)
    zip_code = models.CharField(max_length=100, help_text='Enter Your Zip Code', null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"

