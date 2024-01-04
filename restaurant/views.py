from rest_framework import generics, viewsets
from .models import *
from .serializers import *

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # The ListCreateAPIView automatically provides 'get' and 'post' methods

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # The RetrieveUpdateDestroyAPIView automatically provides 'get', 'put', and 'delete' methods

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
