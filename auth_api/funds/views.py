from funds.models import Fund
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from funds.serializers import FundSerializer
 
 
class FundList(generics.ListCreateAPIView):
    queryset = Fund.objects.all()
    serializer_class = FundSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class FundDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FundSerializer
 
    def get_queryset(self):
        return Fund.objects.all().filter(user=self.request.user)