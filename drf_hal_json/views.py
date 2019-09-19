from rest_framework.mixins import CreateModelMixin
from rest_framework.settings import api_settings
from drf_hal_json import LINKS_FIELD_NAME


class HalCreateModelMixin(CreateModelMixin):
    def get_success_headers(self, data):
        links_data = data.get(LINKS_FIELD_NAME)
        if not links_data:
            return {}
        url_field_data = links_data.get(api_settings.URL_FIELD_NAME)
        if not url_field_data:
            return {}
        return {'Location': str(url_field_data)}
