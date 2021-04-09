from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, MovieSerializer
from .models import Movie


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]