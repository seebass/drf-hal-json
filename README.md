drf-hal-json
=================
Extension for Django REST Framework 3 which allows for using content-type application/hal-json. Its build on top of https://github.com/seebass/drf-nested-fields

## Setup ##

	pip install drf-hal-json
	
	REST_FRAMEWORK = {
    	'DEFAULT_PAGINATION_CLASS': 'drf_hal_json.pagination.HalPageNumberPagination',
    	'DEFAULT_PARSER_CLASSES': ('drf_hal_json.parsers.JsonHalParser',),
    	'DEFAULT_RENDERER_CLASSES': ('drf_hal_json.renderers.JsonHalRenderer',),
	}

## Requirement ##

* Python 2.7+
* Django 1.6+
* Django REST Framework 3
* drf-nested-fields 0.9+

## Features ##

By using the **HalModelSerializer** the Content-Type is application/hal+json.

## Example ##

Serializer:

	class ResourceSerializer(HalModelSerializer):
		class Meta:
			model = Resource

View:
	
	class ResourceViewSet(HalCreateModelMixin, ModelViewSet):
		serializer_class = ResourceSerializer
		queryset = Resource.objects.all()

	GET http://localhost/api/resources/1/ HTTP/1.1
	Content-Type  application/hal+json	

	{
    	"_links": {
        	"self": "http://localhost/api/resources/1/",
			"relatedResource": "http://localhost/api/related-resources/1/"
    	},
    	"id": 1,
    	"_embedded": {
        	"subResource": {
            	"_links": {
                	"self": "http://localhost/resources/1/sub-resources/26/"
                	"subSubResource": "http://localhost/resources/1/sub-resources/26/sub-sub-resources/3"
            	},
            	"id": 26,
            	"name": "Sub Resource 26"
        	}
    	}
	}
