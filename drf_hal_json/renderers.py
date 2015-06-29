from rest_framework.renderers import JSONRenderer

from drf_hal_json import HAL_JSON_MEDIA_TYPE


class JsonHalRenderer(JSONRenderer):
    media_type = HAL_JSON_MEDIA_TYPE
