import limitless

from limitless.api_requestor import APIRequestor
from limitless.limitless_object import LimitlessObject
from limitless.util import convert_to_limitless_object

class APIResource(LimitlessObject):

    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class. You should perform "
                "actions on its subclasses (e.g. Tournament)"
            )
        return "{resource_name}s".format(
            resource_name=cls.RESOURCE_NAME
        )

    @classmethod
    def static_request(cls, method, url, api_token=None, params=None, headers=None):
        requestor = APIRequestor(
            api_token or limitless.api_token
        )
        response = requestor.request(method, url, params)
        limitless_object = convert_to_limitless_object(response,  cls)
        return limitless_object
