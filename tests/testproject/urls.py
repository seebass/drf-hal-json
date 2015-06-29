from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from .views import TestResourceViewSet, RelatedResource1ViewSet, RelatedResource2ViewSet

admin.autodiscover()

router = SimpleRouter()
router.register(r'test-resources', TestResourceViewSet)
router.register(r'related-resources-1', RelatedResource1ViewSet)
router.register(r'related-resources-2', RelatedResource2ViewSet)

urlpatterns = patterns(
    '',
    url(r'', include(router.urls)),
)
