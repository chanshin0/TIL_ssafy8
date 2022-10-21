from rest_framework import serializers
from ..models import Review, Movie

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movie = MovieSerializer(read_only=True) # 리뷰는 many가 될 수 없따!

    class Meta:
        model = Review
        fields = '__all__'