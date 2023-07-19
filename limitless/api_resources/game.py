from limitless import api_endpoints
from limitless import http_methods

from limitless.api_resources.abstract.listable_api_resource import ListableAPIResource


class Game(ListableAPIResource):
    RESOURCE_NAME = "game"

    def get_decks(self, pk):
        pass