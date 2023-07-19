from limitless import http_methods
from limitless.api_requestor import APIRequestor

from limitless.api_resources.abstract.api_resource import APIResource

class ListableAPIResource(APIResource):

    @classmethod
    def list(cls, api_token=None):
        requestor = APIRequestor(api_token)

        url = cls.class_url()
        response = requestor.request(http_methods.HTTP_METHOD_GET, url)
        print(response)
