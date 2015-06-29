from rest_framework.viewsets import ModelViewSet

from drf_hal_json.views import HalCreateModelMixin
from .models import TestResource, RelatedResource2, RelatedResource1
from .serializers import TestResourceSerializer, RelatedResource1Serializer, RelatedResource2Serializer


class TestResourceViewSet(HalCreateModelMixin, ModelViewSet):
    serializer_class = TestResourceSerializer
    queryset = TestResource.objects.all()


class RelatedResource1ViewSet(HalCreateModelMixin, ModelViewSet):
    serializer_class = RelatedResource1Serializer
    queryset = RelatedResource1.objects.all()


class RelatedResource2ViewSet(HalCreateModelMixin, ModelViewSet):
    serializer_class = RelatedResource2Serializer
    queryset = RelatedResource2.objects.all()
