from rest_framework import serializers

from .models import User, Post, Digest


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("content", "rating")


class DigestSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Digest
        fields = ("posts",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        sorted_data = sorted(data["posts"], key=lambda x: x['rating'],
                             reverse=True)
        data["posts"] = [post["content"] for post in sorted_data]
        return data
