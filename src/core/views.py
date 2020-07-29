from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response 
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Mickey',
            'age': 54
        }
        return Response(data)




# Create your views here.
# def test_view(request):
#    data = {
#        'name': 'Mickey',
#        'age': 54
#    }
#    return JsonResponse(data)