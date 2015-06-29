from django.conf import settings

USER_SETTINGS = getattr(settings, "REST_HAL", {})

LINKS_FIELD_NAME = USER_SETTINGS.get("LINKS_FIELD_NAME", "_links")
EMBEDDED_FIELD_NAME = USER_SETTINGS.get("EMBEDDED_FIELD_NAME", "_embedded")

HAL_JSON_MEDIA_TYPE = "application/hal+json"


def is_hal_content_type(content_type):
    return content_type in (HAL_JSON_MEDIA_TYPE, HAL_JSON_MEDIA_TYPE + "; charset=UTF-8")
