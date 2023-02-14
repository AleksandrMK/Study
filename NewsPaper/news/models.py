from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):

    def like(self):
        pass

    def dislike(self):
        pass


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    def like(self):
        pass

    def dislike(self):
        pass
