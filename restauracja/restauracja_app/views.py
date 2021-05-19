from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Kategorie, Dania
from .serializers import KategorieSerializer, DaniaSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import FilterSet, Filter
from rest_framework import permissions
from .custompermission import IsOwnerOrReadOnly
# Create your views here.
#
#@csrf_exempt
# def kategorie_list(request):
#     if request.method == 'GET':
#         kategorieViews = Kategorie.objects.all()
#         serializer = KategorieSerializer(kategorieViews, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = KategorieSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def restauracja_kategorie_detail(request, pk):
#     try:
#         kategorie = Kategorie.objects.get(pk=pk)
#     except Kategorie.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = KategorieSerializer(kategorie)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = KategorieSerializer(kategorie, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         kategorie.delete()
#         return HttpResponse(status=204)
from rest_framework import generics

class RestauracjaKategorieList(generics.ListCreateAPIView):
    queryset = Kategorie.objects.all()
    serializer_class = KategorieSerializer
    view_name = 'kategorie-list'
    filterset_fields = ['Nazwa']
    ordering = ['Nazwa']
    search_fields = ['Nazwa']

class RestauracjaKategorieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kategorie.objects.all()
    serializer_class = KategorieSerializer
    view_name = 'kategorie-detail'

class DaniaFilter(FilterSet):
    min_cena = Filter(field_name = 'Cena', lookup_expr = 'gte')
    max_cena = Filter(field_name = 'Cena', lookup_expr = 'lte')
    class Meta:
        model = Dania
        fields = ['min_cena', 'max_cena']

class DaniaList(generics.ListCreateAPIView):
    queryset = Dania.objects.all()
    serializer_class = DaniaSerializer
    view_name = 'dania-list'
    filter_class = DaniaFilter
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DaniaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dania.objects.all()
    serializer_class = DaniaSerializer
    view_name = 'dania-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ApiRoot(generics.GenericAPIView):
    view_name = 'api-view'
    def get(self, request, *args, **kwargs):
        return Response({
            'kategorie': reverse(RestauracjaKategorieList.view_name, request=request),
            'dania': reverse(DaniaList.view_name, request=request)
        })

