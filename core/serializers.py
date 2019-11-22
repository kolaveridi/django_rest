from rest_framework import serializers
from .models import Customer,Profession,Document,DataSheet

# Serializers define the API representation.
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','address','professions','data_sheet')





class ProfessionaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profession   
        fields=(
            'id','description'
        )     


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model= DataSheet
        fields=(
            'id','historical_data','description'
        )  

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Document
        fields=(
            'id','dtype','doc_number','customer'   
        )            