from rest_framework import serializers
from .models import Customer, Profession, Document, DataSheet


# Serializers define the API representation.
class CustomerSerializer(serializers.ModelSerializer):
    print('xaxxaxxa', Customer)
    num_professions = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('id',
                  'address',
                  'professions',
                  'data_sheet',
                  'active',
                  'status_message',
                  'num_professions'
                  )

    def get_num_professions(self, obj):
        return obj.num_professions()


class ProfessionaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = (
            'id', 'description'
        )


class DataSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = (
            'id', 'historical_data', 'description'
        )


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            'id', 'dtype', 'doc_number', 'customer'
        )
