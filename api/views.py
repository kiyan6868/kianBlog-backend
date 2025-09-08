from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello(request):
    return Response({'message': 'سلام از Django 🚀'})

# Create your views here.
