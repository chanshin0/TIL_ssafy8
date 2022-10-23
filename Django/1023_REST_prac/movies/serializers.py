from .models import Actor, Movie, Review
from rest_framework import serializers

# 여러가지 요청에 대해서 직렬화를 거쳐 JSON을 반환한다. 
# 이렇게 반환되는 씨리얼라이저를 가지고 view함수에서 저장, 조회, 수정,삭제 등 처리를 할 수 있게 되는 거시다.


# Actor
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'
    
    # Movie title 가져오는 부분
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movies = MovieSerializer(many=True, read_only=True) # related_name과 같음

# Movie
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
    
    class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    actors = ActorSerializer(many=True, read_only=True)

    # 리뷰 목록을 가져올때는 리스트
    class ReviewListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')
    review_set = ReviewListSerializer(many=True, read_only=True)


# 리뷰
class ReviewListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MovieSerializer(read_only=True) 
    # 조회하는 1개의 리뷰는 영화 1개에 대한 것이니까 many 옵션이 필요없다.
