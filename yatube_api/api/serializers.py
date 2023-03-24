from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('id', 'text', 'author', 'created', 'post')
        model = Comment
        read_only_fields = ('post', )


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow
        read_only_fields = ('user', )

        validators = (
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Нельзя подписаться второй раз!'
            ),
        )

    def validate_following(self, following):
        if self.context['request'].user == following:
            raise serializers.ValidationError(
                'На самого себя подписаться нельзя!'
            )
        return following
