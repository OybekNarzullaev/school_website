import os.path
from django.db import models
from django.contrib.auth.models import User


def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]

    if instance.pk:
        filename = 'ser_Profile_Pictures/{}.{}'.format(instance.pk, ext)

    return os.path.join(upload_to, filename)


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.CharField(max_length=500)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)

    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent'),
    ]

    user_type = models.CharField(max_length=10, choices=user_types, default=student)

    def __str__(self):
        return self.user.username

def save_news_image(instance, filename):
    upload_to = 'Images/news/'
    ext = filename.split('.')[-1]  # fan.jpg -> ['fan', 'jpg']

    # fayl nominini olish
    if instance.id:
        filename = '{}.{}'.format(instance.id, ext)
    return os.path.join(upload_to, filename)

class New(models.Model):
    title = models.CharField(max_length=100, unique=True)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=save_news_image)