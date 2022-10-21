from rest_framework import serializers
from ..models import Movie, Actor, Review


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class MovieSerializer(serializers.ModelSerializer):

    # 무비 가져올 떄 배우 이름과 리뷰 제목,내용도 함께 가져오려고 작성한 것
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class ReviewListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')

    actors = ActorSerializer(many=True, read_only=True)
    review_set = ReviewListSerializer(many=True, read_only=True)
    

    class Meta:
        model = Movie
        fields = '__all__'