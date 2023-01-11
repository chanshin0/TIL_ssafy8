# serializer : 모델에서 데이터 가져와서 json으로 바꾸는 것
# 쿼리문으로 구성된 데이터를 JSON 포맷으로 쉽게 변환해주는 객체
from rest_framework import serializers
from ..models import Actor, Movie

class ActorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        # fields = '__all__'
        fields = ('name', )

class ActorSerializer(serializers.ModelSerializer):
    
    # Movie의 title을 가져오기 위해서 사용
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title', )
            
    # related_name이랑 같아야함!
    movies = MovieSerializer(many=True, read_only = True)

    class Meta:
        model = Actor
        fields = '__all__'
