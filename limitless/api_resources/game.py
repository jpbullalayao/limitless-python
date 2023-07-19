from limitless import api_endpoints
from limitless import http_methods
from limitless.api_requestor import APIRequestor

from limitless.api_resources.abstract.listable_api_resource import ListableAPIResource
from limitless.util import convert_to_limitless_object

class Game(ListableAPIResource):
    RESOURCE_NAME = "game"
    FIELD_PK = "id"

    @classmethod
    def base_url(cls, pk):
        base_url = cls.class_url()

        return f"{base_url}/{pk}"

    @classmethod
    def get_decks(cls, api_token=None, **params):
        requestor = APIRequestor(api_token)

        pk = params.get(Game.FIELD_PK)
        url = Game.base_url(pk) + api_endpoints.GAME_DECKS
        response = requestor.request(http_methods.HTTP_METHOD_GET, url)
        limitless_object = convert_to_limitless_object(response, cls)

        return limitless_object
