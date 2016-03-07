from collections import OrderedDict

from rest_framework.fields import empty
from rest_framework.relations import RelatedField, ManyRelatedField, HyperlinkedRelatedField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, BaseSerializer
from rest_framework.settings import api_settings
from drf_nested_fields.serializers import NestedFieldsSerializerMixin

from drf_hal_json import LINKS_FIELD_NAME, EMBEDDED_FIELD_NAME


class HalEmbeddedSerializer(NestedFieldsSerializerMixin, ModelSerializer):
    pass


class HalModelSerializer(NestedFieldsSerializerMixin, ModelSerializer):
    """
    Serializer for HAL representation of django models
    """
    serializer_related_field = HyperlinkedRelatedField
    links_serializer_class = HyperlinkedModelSerializer
    embedded_serializer_class = HalEmbeddedSerializer

    def __init__(self, instance=None, data=empty, **kwargs):
        super(HalModelSerializer, self).__init__(instance, data, **kwargs)
        self.nested_serializer_class = self.__class__
        if data != empty and not LINKS_FIELD_NAME in data:
            data[LINKS_FIELD_NAME] = dict()  # put links in data, so that field validation does not fail

    def get_fields(self):
        fields = super(HalModelSerializer, self).get_fields()

        embedded_field_names = list()
        link_field_names = list()
        resulting_fields = OrderedDict()
        resulting_fields[LINKS_FIELD_NAME] = None  # assign it here because of the order -> links first

        for field_name, field in fields.items():
            if self._is_link_field(field):
                link_field_names.append(field_name)
            elif self._is_embedded_field(field):
                embedded_field_names.append(field_name)
            else:
                resulting_fields[field_name] = field

        links_serializer = self._get_links_serializer(self.Meta.model, link_field_names)
        if not links_serializer:
            # in case the class is overridden and the inheriting class wants no links to be serialized, the links field is removed
            del resulting_fields[LINKS_FIELD_NAME]
        else:
            resulting_fields[LINKS_FIELD_NAME] = links_serializer
        if embedded_field_names:
            resulting_fields[EMBEDDED_FIELD_NAME] = self._get_embedded_serializer(self.Meta.model, getattr(self.Meta, "depth", 0),
                                                                                  embedded_field_names)
        return resulting_fields

    def _get_links_serializer(self, model_cls, link_field_names):
        class HalNestedLinksSerializer(self.links_serializer_class):
            serializer_related_field = self.serializer_related_field
            serializer_url_field = self.serializer_url_field

            class Meta:
                model = model_cls
                fields = [api_settings.URL_FIELD_NAME] + link_field_names
                extra_kwargs = getattr(self.Meta, 'extra_kwargs', {})

        return HalNestedLinksSerializer(instance=self.instance, source="*")

    def _get_embedded_serializer(self, model_cls, embedded_depth, embedded_field_names):
        defined_nested_fields = getattr(self.Meta, "nested_fields", None)
        nested_class = self.__class__

        class HalNestedEmbeddedSerializer(self.embedded_serializer_class):
            nested_serializer_class = nested_class

            class Meta:
                model = model_cls
                fields = embedded_field_names
                nested_fields = defined_nested_fields
                depth = embedded_depth
                extra_kwargs = getattr(self.Meta, 'extra_kwargs', {})

        return HalNestedEmbeddedSerializer(source="*")

    @staticmethod
    def _is_link_field(field):
        return isinstance(field, RelatedField) or isinstance(field, ManyRelatedField) \
               or isinstance(field, HyperlinkedIdentityField)

    @staticmethod
    def _is_embedded_field(field):
        return isinstance(field, BaseSerializer)
