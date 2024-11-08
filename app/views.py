from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Laptop
from .serializers import LaptopSerializer

class LaptopListView(APIView):
    def get(self, request):
        laptops = Laptop.objects.all()
        serializer = LaptopSerializer(laptops, many=True)
        return Response(serializer.data)

class LaptopCreateView(APIView):
    def post(self, request):
        serializer = LaptopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaptopDetailView(APIView):
    def get(self, request, pk):
        try:
            laptop = Laptop.objects.get(pk=pk)
        except Laptop.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LaptopSerializer(laptop)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LaptopUpdateView(APIView):
    def put(self, request, pk):
        try:
            laptop = Laptop.objects.get(pk=pk)
        except Laptop.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LaptopSerializer(laptop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LaptopDeleteView(APIView):
    def delete(self, request, pk):
        try:
            laptop = Laptop.objects.get(pk=pk)
        except Laptop.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        
        laptop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)