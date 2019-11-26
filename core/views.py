
from rest_framework.response import Response
from .models import Customer,Profession,DataSheet,Document
from .serializers import CustomerSerializer,ProfessionaSerializer,DataSheetSerializer,DocumentSerializer
from rest_framework import  viewsets
from django.http.response import HttpResponseNotAllowed


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class=CustomerSerializer
    def get_queryset(self):
        active_customers=Customer.objects.filter(active=True)
        for x in range(len(active_customers)): 
                        print(active_customers[x])
        return active_customers


    def list(self,request,*args,**kwargs):
        #import pdb; pdb.set_trace()
        customers =Customer.objects.filter(id=7)
        serializer=CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, *args, **kwargs):
        """obj=self.get_object()
        print('obj is ',obj)
        serializer = CustomerSerializer(obj)
        print('serializer.data is ', serializer.data)
        return Response(serializer.data)"""
        return HttpResponseNotAllowed('Not Allowed')

    
    
class ProfessionViewSet(viewsets.ModelViewSet):
    queryset=Profession.objects.all()
    serializer_class =ProfessionaSerializer
    
    
class DataSheetViewSet(viewsets.ModelViewSet):
    queryset=DataSheet.objects.all() 
    serializer_class= DataSheetSerializer
    
    
    
class DocumentViewSet(viewsets.ModelViewSet):
    queryset=Document.objects.all()
    serializer_class=DocumentSerializer
    
       
    
        