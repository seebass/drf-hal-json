from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter
from .views import TestResourceViewSet, RelatedResource1ViewSet, RelatedResource2ViewSet

router = SimpleRouter()
router.register(r'test-resources', TestResourceViewSet)
router.register(r'related-resources-1', RelatedResource1ViewSet)
router.register(r'related-resources-2', RelatedResource2ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
