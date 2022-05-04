from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio

class Person(APIView):
    def get(self, request):
        return Response(data="Hola! Soy una persona", status=200)
    def patch(self, request):
        return Response(data="Parchando persona", status=200)
    def delete(self, request):
        return Response(data="Persona eliminada con exito", status=200)
    def post(self, request):
        return Response(data="Persona agregada exitosamente!", status=200)

class Pet(APIView):
    def get(self, request):
        return Response(data="Hola! Soy una mascota", status=200)
    def patch(self, request):
        return Response(data="Parchando mascota", status=200)
    def delete(self, request):
        return Response(data="Mascota eliminada con exito", status=200)
    def post(self, request):
        return Response(data="Mascota agregada exitosamente!", status=200)