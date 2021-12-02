from rest_framework.serializers import ModelSerializer, CharField
from .models import Manufacturer, Molding


class ManufacturerSerializer(ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ['id', 'title', 'city', 'address', 'phone']


class MoldingSerializer(ModelSerializer):

    manufacturer = CharField(source='manufacturer.title')

    class Meta:
        model = Molding
        fields = ['id', 'manufacturer', 'title', 'code', 'color', 'price']

    def create(self, validated_data):
        manufacturer = validated_data.get('manufacturer').get('title')
        manufacturer = Manufacturer.objects.filter(title=manufacturer).first()
        validated_data['manufacturer'] = manufacturer
        molding = self.Meta.model(**validated_data)
        molding.save()
        return molding
