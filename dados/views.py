from distutils.file_util import write_file
from django.shortcuts import render
from rest_framework import views
from .serializers import DadoSerializer,ListDadoSerializer
from django.core.files.storage import default_storage
from rest_framework.generics import ListAPIView
import  datetime as dt
import pandas as pd
from .models import Dado

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

        dados = resquest.data.get('file', default=None)
       
        if dados is None:
            return views.Response(
                data={'file':'This field is required.'},
                status = views.status.HTTP_400_BAD_REQUEST,
            )

        with default_storage.open('CNAB.txt' , 'wb+') as arq:
            for chunk in dados.chunks():
                arq.write(chunk)
        
        with open('CNAB.txt','r', encoding="utf-8")as text_list:
            file = [item for item in text_list ]
            result = []

          
            for line in file:
                size = 0 
                dict_text = {}
                for index, sizeSum in enumerate(cut_size):
                    dict_text.update({f"{table_camp[index]}":line[size:size+sizeSum]})
                    size += sizeSum
                result.append(dict_text)
            
        for item in result:
            item['date'] = pd.to_datetime(item['date'],format='%Y%m%d')
            item['value'] = int(item['value'])/100
            item['hour'] = f"{item['hour'][0:2]}:{item['hour'][2:4]}:{item['hour'][4:6]}"
            item['store_owner'] = item['store_owner'].rstrip()
            item['store_name'] = item['store_name'].rstrip()

        data_result =[]
        for item in result:
            act_item = Dado.objects.create(**item)
            data_result.append(act_item)
            

        serializer = DadoSerializer(data= data_result, many=True)
        serializer.is_valid()

        return views.Response(serializer.data, views.status.HTTP_201_CREATED)

class ListDados(ListAPIView):
    queryset = Dado.objects.all()
    serializer_class =  ListDadoSerializer