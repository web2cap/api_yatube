# import datetime as dt

from rest_framework import serializers

from posts.models import Comment, Group, Post, User

# from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):
    cats = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            # "cats"
        )
        ref_name = "ReadOnlyUsers"


class CommentSerializer(serializers.ModelSerializer):
    # меняем имя поля
    # achievement_name = serializers.CharField(source="name")

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "text", "pub_date", "author", "image", "group")
