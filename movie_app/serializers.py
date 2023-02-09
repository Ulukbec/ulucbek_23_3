from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = "id name quantity_movies".split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'text stars movie_id'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer().fields.get('name')

    class Meta:
        model = Movie
        fields = 'id title description duration director rating'.split()


class MovieReviewSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)
    director = DirectorSerializer().fields.get('name')

    class Meta:
        model = Movie
        fields = 'id title description duration director movie_reviews rating'.split()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1)
    description = serializers.CharField(min_length=1)
    duration = serializers.FloatField()
    director_id = serializers.IntegerField()

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f"Director with ({director_id}) does not exists")
        return director_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=1)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    movie_id = serializers.IntegerField()
