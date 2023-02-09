from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView


class DirectorListAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        serializer = DirectorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'error': serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = serializer.validated_data.get("name")
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={"message": "data received",
                              "post": DirectorSerializer(director).data})


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


# @api_view(['GET', "POST"])
# def director_view(request):
#     if request.method == "GET":
#         director = Director.objects.all()
#         serializer = DirectorSerializer(director, many=True)
#         return Response(data=serializer.data)
#     elif request.method == "POST":
#         serializer = DirectorSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(data={'error': serializer.errors},
#                             status=status.HTTP_406_NOT_ACCEPTABLE)
#         name = serializer.validated_data.get("name")
#         director = Director.objects.create(name=name)
#         director.save()
#         return Response(data={"message": "data received",
#                               "post": DirectorSerializer(director).data})


# @api_view(['GET', "DELETE", "PUT"])
# def directors_detail_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response(data={'error': "Director not found"},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = DirectorSerializer(director, many=False)
#         return Response(data=serializer.data)
#     elif request.method == "DELETE":
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         director.name = request.data.get("name")
#         director.save()
#         return Response(data={"message": "director updated successfully !",
#                               "director": DirectorSerializer(director).data})

class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"error": serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = serializer.validated_data.get("title")
        description = serializer.validated_data.get("description")
        duration = serializer.validated_data.get("duration")
        director_id = serializer.validated_data.get("director_id")
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data={"message": "data required",
                              "movie": MovieSerializer(movie).data})


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


# @api_view(['GET', "PUT", "DELETE"])
# def movies_detail_view(request, id):
#     try:
#         movies = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(data={'error': "Director not found"},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = MovieSerializer(movies, many=False)
#         return Response(data=serializer.data)
#     elif request.method == "DELETE":
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == "PUT":
#         movies.title = request.data.get("title")
#         movies.description = request.data.get("description")
#         movies.duration = request.data.get("duration")
#         movies.director_id = request.data.get("director_id")
#         movies.save()
#         return Response(data={"message": "movie updated successfully",
#                               "movie": MovieSerializer(movies).data})

class ReviewAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={"errors": serializer.errors},
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        text = serializer.validated_data.get("text")
        stars = serializer.validated_data.get("stars", 0)
        movie_id = serializer.validated_data.get("movie_id", 1)
        review = Review.objects.create(text=text, stars=stars, movie_id=movie_id)
        review.save()
        return Response(data={"message": "data required",
                              "review": ReviewSerializer(review).data})


class MovieReviewAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieReviewSerializer


# @api_view(["GET"])
# def movie_review_view(request):
#     if request.method == "GET":
#         movie = Movie.objects.all()
#         serializer = MovieReviewSerializer(movie, many=True)
#         return Response(data=serializer.data)

class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = "id"

# @api_view(['GET', "PUT", "DELETE"])
# def review_detail_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist:
#         return Response(data={'error': "Review not found"},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == "GET":
#         serializer = ReviewSerializer(review, many=False)
#         return Response(data=serializer.data)
#     elif request.method == "PUT":
#         review.text = request.data.get("text")
#         review.save()
#         return Response(data={"message": "review updated successfully",
#                               "review": ReviewSerializer(review).data})
#     else:
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
