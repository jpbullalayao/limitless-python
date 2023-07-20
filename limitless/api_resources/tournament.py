from limitless import api_endpoints
from limitless import http_methods

from limitless.api_resources.abstract.listable_api_resource import ListableAPIResource
class Tournament(ListableAPIResource):
    RESOURCE_NAME = "tournament"
    FIELD_PK = "id"

    @classmethod
    def base_url(cls, pk):
        base_url = cls.class_url()

        return f"{base_url}/{pk}"

    @classmethod
    def get_details(cls, api_token=None, **params):
        pk = params.get(Tournament.FIELD_PK)
        url = Tournament.base_url(pk) + api_endpoints.TOURNAMENT_DETAILS
        response = cls.static_request(http_methods.HTTP_METHOD_GET, url, api_token)

        return response

    @classmethod
    def get_standings(cls, api_token=None, **params):
        pk = params.get(Tournament.FIELD_PK)
        url = Tournament.base_url(pk) + api_endpoints.TOURNAMENT_STANDINGS
        response = cls.static_request(http_methods.HTTP_METHOD_GET, url, api_token)

        return response

    @classmethod
    def get_pairings(cls, api_token=None, **params):
        pk = params.get(Tournament.FIELD_PK)
        url = Tournament.base_url(pk) + api_endpoints.TOURNAMENT_PAIRINGS
        response = cls.static_request(http_methods.HTTP_METHOD_GET, url, api_token)

        return response
