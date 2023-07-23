from django.contrib import admin
from django.apps import apps
from .models import (
    User, Post, Subscription, Digest, PostToDigest
)


for app_config in apps.get_app_configs():
    [admin.site.unregister(model) for model in app_config.get_models() if
     admin.site.is_registered(model)]

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Subscription)
admin.site.register(Digest)
admin.site.register(PostToDigest)
