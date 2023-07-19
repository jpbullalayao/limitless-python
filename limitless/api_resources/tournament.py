from limitless import api_endpoints
from limitless import http_methods

from limitless.api_resources.abstract.listable_api_resource import ListableAPIResource
class Tournament(ListableAPIResource):
    RESOURCE_NAME = "tournament"

    def get_details(self, pk):
        pass

    def get_standings(self, pk):
        pass

    def get_pairings(self, pk):
        pass

