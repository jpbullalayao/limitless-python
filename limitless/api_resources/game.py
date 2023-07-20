from limitless import api_endpoints
from limitless import http_methods

from limitless.api_resources.abstract.listable_api_resource import ListableAPIResource

class Game(ListableAPIResource):
    RESOURCE_NAME = "game"
    FIELD_PK = "id"

    @classmethod
    def base_url(cls, pk):
        base_url = cls.class_url()

        return f"{base_url}/{pk}"

    @classmethod
    def get_decks(cls, api_token=None, **params):
        pk = params.get(Game.FIELD_PK)
        url = Game.base_url(pk) + api_endpoints.GAME_DECKS
        response = cls.static_request(http_methods.HTTP_METHOD_GET, url, api_token)

        return response
