from django.db import models
from django.utils.translation import gettext_lazy as _

CHOICES = (
    [(i, i) for i in range(1, 11)]
)


class User(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': _("A user with that name already exists."),
        },
    )

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user"
    )
    source = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.name} subscription: №{self.id}"


class Post(models.Model):
    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.CASCADE,
        related_name="post"
    )
    content = models.TextField()
    rating = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return f"{self.subscription.user.name} " \
               f"subscription id:{self.subscription.id} post id:{self.id}"


class Digest(models.Model):
    posts = models.ManyToManyField(
        Post,
        through="PostToDigest",
        related_name="digest"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class PostToDigest(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    digests = models.ForeignKey(Digest, on_delete=models.CASCADE)
