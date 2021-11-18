# django rest frameworks
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

# models
from visits.serializer import VisitsModelsSerializers
# models
from visits.models import VisitsModels


class VisitsViewSets(APIView):
    parser_classes = (MultiPartParser,FormParser,JSONParser)

    def get(self, request, format=None):
        """
        Return count vists.
        """
        queryset = VisitsModels.objects.all()
        visits = VisitsModelsSerializers(queryset,many=True)
        return Response(len(visits.data))
    def post(self, request, format=None):
        """
        create visit.
        """
        ip,created =VisitsModels.objects.get_or_create(ip_adreess=request.headers["X-Real-IP"])
        return Response(ip.ip_adreess)