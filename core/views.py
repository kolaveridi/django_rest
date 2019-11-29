from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Customer, Profession, DataSheet, Document
from .serializers import CustomerSerializer, ProfessionaSerializer, DataSheetSerializer, DocumentSerializer
from rest_framework import viewsets
from django.http.response import HttpResponseNotAllowed
from django.http.response import HttpResponseNotAllowed


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        #import pdb;pdb.set_trace()
        # active_customers = Customer.objects.filter(active=True)
        # for x in range(len(active_customers)):
        #     print(active_customers[x])
        # return active_customers
        address = self.request.query_params.get('address', None)
        #import pdb;pdb.set_trace()
        if self.request.query_params.get('active') == 'False':
            status=False
        else:
            status=True

        if address:
            print("status",status)
            customers=Customer.objects.filter(address_icontains=address ,active=status)
        else:
            print("status", status)
            customers=Customer.objects.filter(active=False)

        # serializer = CustomerSerializer(customers, many=True)
        # return Response(serializer.data)
        return customers

    # def list(self, request, *args, **kwargs):
    #     # import pdb;
    #     # pdb.set_trace()
    #
    #
    #     # customers = Customer.objects.all()
    #     # id=self.request.query_params.get('id',None)
    #     # status=True if self.request.query_params.get('active') == 'True' else False
    #     # print("status",status)
    #     # if id:
    #     #     customers = Customer.objects.filter(id=id, active=status)
    #     # else:
    #     #     customers = Customer.objects.filter(active=status)
    #
    #     address=self.request.query_params.get('address',None)
    #     print("address", address)
    #     import pdb;pdb.set_trace()
    #     if self.request.query_params.get('active') == 'False':
    #         status=False
    #     else:
    #         status=True
    #
    #     if address:
    #         customers=Customer.objects.filter(address_icontains=address ,active=status)
    #     else:
    #         customers=Customer.objects.filter(active=status)
    #
    #     serializer = CustomerSerializer(customers, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        """obj=self.get_object()
        print('obj is ',obj)
        serializer = CustomerSerializer(obj)
        print('serializer.data is ', serializer.data)
        return Response(serializer.data)"""
        return HttpResponseNotAllowed('Not Allowed')

    def create(self, request, *args, **kwargs):
        data = request.data
        print('request', request)
        customer = Customer.objects.create(
            name=data['name'],
            address=data['address'],
            data_sheet_id=data['data_sheet']
        )
        print('data', data)
        profession = Profession.objects.get(id=data['profession'])
        customer.professions.add(profession)
        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        customer = self.get_object()
        print('customer', customer)
        data = request.data
        customer.name = data['name']
        customer.address = data['address']
        customer.data_sheet_id = data['data_sheet']

        profession = Profession.objects.get(id=data['profession'])

        for p in customer.professions.all():
            customer.professions.remove(p)

        customer.professions.add(profession)
        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.name = request.data.get('name', customer.name)
        customer.address = request.data.get('address', customer.address)
        customer.data_sheet_id = request.data.get('data_sheet', customer.data_sheet_id)
        customer.save()
        print('customer is ', customer)
        serializer = CustomerSerializer(customer)
        print('data inside is ', serializer.data)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.delete()
        return Response('Object Removed')

    @action(detail=True)
    def deactivate(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.active = False
        serializer = CustomerSerializer(customer)
        print('data inside is ', serializer.data)
        return Response(serializer.data)


    @action(detail=False)
    def deactivate_all(self,request,*args,**kwargs):
        #import pdb;pdb.set_trace()
        customer=Customer.objects.all()
        customer.update(active=False)
        serializer=CustomerSerializer(customer,many=True)
        return Response(serializer.data)

    @action(detail=False)
    def activate_all(self, request, *args, **kwargs):
        customer = Customer.objects.all()
        customer.update(active=True)
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    @action(detail=False,methods=['POST'])
    def change_status(self,request,*args,**kwargs):
        #import pdb;pdb.set_trace()
        status=request.data['active']
        customers=Customer.objects.all()
        print('customers',customers)
        for x in range(len(customers)):
            print(customers[x].active)
        customers.update(active=status)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionaSerializer


class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
