# django rest frameworks
from datetime import datetime
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

#serializer
from commentaries.serializer import CommentariesModelsSerializers

# models
from commentaries.models import CommentariesModels


class CommentariesViewSets(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    queryset = CommentariesModels.objects.filter(is_activate=True)
    serializer_class = CommentariesModelsSerializers
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'