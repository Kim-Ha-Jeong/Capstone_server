from rest_framework import viewsets
#from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend
from api.filter import *
from api.serializers import *

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # parser_classes = [MultiPartParser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter


class FullViewSet(viewsets.ModelViewSet):
    queryset = Full.objects.all()
    serializer_class = FullSerializer


class EditedViewSet(viewsets.ModelViewSet):
    queryset = Edited.objects.all()
    serializer_class = EditedSerializer

