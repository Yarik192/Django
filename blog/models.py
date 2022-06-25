from django.db import models
from django.utils import timezone
from datetime import timedelta


class User(models.Model):
    nickname = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname


class Comment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=30, blank=True)
    comment = models.TextField()
    create_published = models.DateField(default=timezone.now)
    updated_published = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.updated_published = timezone.now().date() - timedelta(days=365)
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.header


class ReplyToComment(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=30, blank=True)
    comment_which_reply = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment = models.TextField()
    like = models.BooleanField("Лайк", default=False)
    dislike = models.BooleanField("Дизлайк", default=False)

    def __str__(self):
        return f"{self.header} reply to {self.comment_which_reply}"



