from rest_framework import generics
from .models import TodoModel
from .serializers import TodoSerializers


# Create your views here.


class HomeApiViews(generics.ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class TDetailApiViews(generics.RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class TUpdateApiViews(generics.UpdateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers


class TCreateApiViews(generics.CreateAPIView):
    serializer_class = TodoSerializers


class TDeleteApiViews(generics.DestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializers

