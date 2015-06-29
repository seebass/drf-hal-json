from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.settings import api_settings

from drf_hal_json import LINKS_FIELD_NAME, EMBEDDED_FIELD_NAME
from .models import TestResource, RelatedResource1, RelatedResource2


class HalTest(TestCase):
    TESTSERVER_URL = "http://testserver"

    def setUp(self):
        self.related_resource_1 = RelatedResource1.objects.create(name="Related-Resource1")
        self.nested_related_resource_1_1 = RelatedResource1.objects.create(name="Nested-Related-Resource11")
        self.nested_related_resource_1_2 = RelatedResource1.objects.create(name="Nested-Related-Resource12")
        self.related_resource_2 = RelatedResource2.objects.create(name="Related-Resource2")
        self.related_resource_2.related_resources_1.add(self.nested_related_resource_1_1, self.nested_related_resource_1_2)
        self.test_resource_1 = TestResource.objects.create(name="Test-Resource", related_resource_1=self.related_resource_1,
                                                           related_resource_2=self.related_resource_2)

    def testGetHalResource(self):
        resp = self.client.get("/test-resources/")
        self.assertEqual(200, resp.status_code, resp.content)
        self.assertEqual(1, len(resp.data))
        test_resource_data = resp.data[0]
        self.assertEqual(4, len(test_resource_data))
        self.assertEqual(self.test_resource_1.id, test_resource_data['id'])
        self.assertEqual(self.test_resource_1.name, test_resource_data['name'])
        test_resource_links = test_resource_data[LINKS_FIELD_NAME]
        self.assertEqual(2, len(test_resource_links))
        self.assertEqual(self.TESTSERVER_URL + reverse('testresource-detail', kwargs={'pk': self.test_resource_1.id}),
                         test_resource_links[api_settings.URL_FIELD_NAME])
        self.assertEqual(self.TESTSERVER_URL + reverse('relatedresource1-detail', kwargs={'pk': self.related_resource_1.id}),
                         test_resource_links['related_resource_1'])

        related_resource_2_data = test_resource_data[EMBEDDED_FIELD_NAME]['related_resource_2']
        self.assertEqual(3, len(related_resource_2_data))
        self.assertEqual(self.related_resource_2.name, related_resource_2_data['name'])
        related_resource_2_links = related_resource_2_data[LINKS_FIELD_NAME]
        self.assertEqual(1, len(related_resource_2_links))
        self.assertEqual(self.TESTSERVER_URL + reverse('relatedresource2-detail', kwargs={'pk': self.related_resource_2.id}),
                         related_resource_2_links[api_settings.URL_FIELD_NAME])
        related_resource_2_embedded = related_resource_2_data[EMBEDDED_FIELD_NAME]
        self.assertEqual(1, len(related_resource_2_embedded))
        nested_related_resources_data = related_resource_2_embedded['related_resources_1']
        self.assertEqual(2, len(nested_related_resources_data))
        self.assertEqual(3, len(nested_related_resources_data[0]))
        self.assertEqual(3, len(nested_related_resources_data[1]))
        self.assertEqual(self.nested_related_resource_1_1.id, nested_related_resources_data[0]['id'])
        self.assertEqual(self.nested_related_resource_1_1.name, nested_related_resources_data[0]['name'])
        self.assertEqual(
            self.TESTSERVER_URL + reverse('relatedresource1-detail', kwargs={'pk': self.nested_related_resource_1_1.id}),
            nested_related_resources_data[0][LINKS_FIELD_NAME][api_settings.URL_FIELD_NAME])
        self.assertEqual(self.nested_related_resource_1_2.id, nested_related_resources_data[1]['id'])
        self.assertEqual(self.nested_related_resource_1_2.name, nested_related_resources_data[1]['name'])
        self.assertEqual(
            self.TESTSERVER_URL + reverse('relatedresource1-detail', kwargs={'pk': self.nested_related_resource_1_2.id}),
            nested_related_resources_data[1][LINKS_FIELD_NAME][api_settings.URL_FIELD_NAME])
