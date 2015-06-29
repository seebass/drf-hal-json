from drf_hal_json.serializers import HalModelSerializer
from .models import TestResource, RelatedResource2, RelatedResource1


class TestResourceSerializer(HalModelSerializer):
    class Meta:
        model = TestResource
        fields = ('id', 'name', 'related_resource_1')
        nested_fields = {
            'related_resource_2': (
                ['name'],
                {
                    'related_resources_1': (
                        ['id', 'name'],
                        {}
                    )
                })
        }


class RelatedResource1Serializer(HalModelSerializer):
    class Meta:
        model = RelatedResource1


class RelatedResource2Serializer(HalModelSerializer):
    class Meta:
        model = RelatedResource2
