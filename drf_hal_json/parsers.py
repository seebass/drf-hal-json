from rest_framework.parsers import JSONParser
from drf_hal_json import HAL_JSON_MEDIA_TYPE

from drf_hal_json.renderers import JsonHalRenderer


class JsonHalParser(JSONParser):
    media_type = HAL_JSON_MEDIA_TYPE
    renderer_class = JsonHalRenderer
