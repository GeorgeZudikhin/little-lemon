from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # The ListCreateAPIView automatically provides 'get' and 'post' methods

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # The RetrieveUpdateDestroyAPIView automatically provides 'get', 'put', and 'delete' methods