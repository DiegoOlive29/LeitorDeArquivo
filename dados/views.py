from distutils.file_util import write_file
from django.shortcuts import render
from rest_framework import views
from .serializers import DadoSerializer
from django.core.files.storage import default_storage
import  pandas as  pd

# Create your views here.
cut_size = [1,8,10,11,12,6,14,19]
table_camp = [
    'typeOp',
    'date',
    'value',
    'cpf',
    'card',
    'hour',
    'store_owner',
    'store_name',

]

class DadosView(views.APIView):


    def post(self, resquest:views.Request,format=None) -> views.Response:

        serializer = DadoSerializer

        dados = resquest.data.get("file", default=None)
       
        if dados is None:
            return views.Response(
                data={'file':'This field is required.'},
                status = views.status.HTTP_400_BAD_REQUEST,
            )

        with default_storage.open("CNAB.txt" , "wb+") as arq:
            for chunk in dados.chunks():
                arq.write(chunk)
        
        with open('CNAB.txt','r', encoding="utf-8")as text_list:
            file = [item for item in text_list ]
            result = []

            dict_text = {}
            for line in file:
                size = 0 
                for index, sizeSum in enumerate(cut_size):
                    dict_text.update({f"{table_camp[index]}":line[size:size+sizeSum]})
                    size += sizeSum
                result.append(dict_text)


            
         
        

        return views.Response(result, views.status.HTTP_201_CREATED)