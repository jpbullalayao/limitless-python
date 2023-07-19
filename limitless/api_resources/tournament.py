from limitless import api_endpoints
from limitless import http_methods
from limitless.api_requestor import APIRequestor

from limitless.api_resources.abstract.listable_api_resource import ListableAPIResource
from limitless.util import convert_to_limitless_object
class Tournament(ListableAPIResource):
    RESOURCE_NAME = "tournament"
    FIELD_PK = "id"

    @classmethod
    def base_url(cls, pk):
        base_url = cls.class_url()

        return f"{base_url}/{pk}"

    @classmethod
    def get_details(cls, api_token=None, **params):
        requestor = APIRequestor(api_token)

        pk = params.get(Tournament.FIELD_PK)
        url = Tournament.base_url(pk) + api_endpoints.TOURNAMENT_DETAILS
        response = requestor.request(http_methods.HTTP_METHOD_GET, url)
        limitless_object = convert_to_limitless_object(response, cls)

        return limitless_object

    @classmethod
    def get_standings(cls, api_token=None, **params):
        requestor = APIRequestor(api_token)

        pk = params.get(Tournament.FIELD_PK)
        url = Tournament.base_url(pk) + api_endpoints.TOURNAMENT_STANDINGS
        response = requestor.request(http_methods.HTTP_METHOD_GET, url)
        limitless_object = convert_to_limitless_object(response, cls)

        return limitless_object

    @classmethod
    def get_pairings(cls, api_token=None, **params):
        requestor = APIRequestor(api_token)

        pk = params.get(Tournament.FIELD_PK)
        url = Tournament.base_url(pk) + api_endpoints.TOURNAMENT_PAIRINGS
        response = requestor.request(http_methods.HTTP_METHOD_GET, url)
        limitless_object = convert_to_limitless_object(response, cls)

        return limitless_object
