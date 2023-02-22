from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PeopleSerializer
from .models import People


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/people-list/',
        'Detail view' : '/people-detail/<int:id>/',
        'Create' : '/people-create/',
        'Update' : '/people-update/<int:id>/',
        'Delete' : '/people-delete/<int:id>',
    }
    
    return Response(api_urls);

@api_view(['GET'])
def ShowAll(request):
    peoples = People.objects.all()
    serializer = PeopleSerializer(peoples,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewPeople(request,pk):
    peoples = People.objects.get(id=pk)
    serializer = PeopleSerializer(peoples,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AddPeople(request):
    serializer = PeopleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def UpdatePeople(request,pk):
    peoples = People.objects.get(id=pk)
    serializer = PeopleSerializer(instance=peoples,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET']) 
def DeletePeople(request,pk):
    peoples = People.objects.get(id=pk)
    peoples.delete()

    return Response('people deleted successfully')
    