from posts.models import Comment, Group, Post, User
from rest_framework import serializers


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
    author = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
        read_only_fields = ("author",)

    def get_author(self, obj):
        return obj.author.username


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "text", "pub_date", "author", "image", "group")

    def get_author(self, obj):
        return obj.author.username
