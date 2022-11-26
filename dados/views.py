from distutils.file_util import write_file
from django.shortcuts import render
from rest_framework import views
from .serializers import DadoSerializer
# Create your views here.

class DadosView(views.APIView):

    def post(self, resquest:views.Request,format=None) -> views.Response:

        serializer = DadoSerializer

        dados = resquest.data.get("file", default=None)
       
        if dados is None:
            return views.Response(
                data={'file':'This field is required.'},
                status = views.status.HTTP_400_BAD_REQUEST,
            )

        

        

        return views.Response(dados, views.status.HTTP_201_CREATED)