from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User, Post, Digest
from .serializers import UserSerializer, DigestSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=("get",))
    def digest(self, request, pk):
        posts = Post.objects.filter(subscription__user=int(pk))
        rating = request.query_params.get("rating")
        if rating:
            if rating.isdigit() and int(rating) in range(1, 11):
                sorted_posts = posts.filter(
                    rating__gte=int(rating)
                )
                return self.add_digest(sorted_posts, pk)
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            return self.add_digest(posts, pk)

    def add_digest(self, posts, pk):
        digest, _ = Digest.objects.get_or_create(
            user=User.objects.get(id=int(pk)),
        )
        digest.posts.set(posts)
        serializer = DigestSerializer(digest)
        return Response(serializer.data, status=status.HTTP_200_OK)
