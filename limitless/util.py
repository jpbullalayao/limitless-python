from limitless.limitless_response import LimitlessResponse
from limitless.limitless_object import LimitlessObject


def convert_to_limitless_object(resp, cls):
    if isinstance(resp, LimitlessResponse):
        limitless_response = resp
        resp = limitless_response.data

    if isinstance(resp, list):
        return [
            convert_to_limitless_object(result, cls) for result in resp
        ]

    elif isinstance(resp, dict) and not isinstance(
        resp, LimitlessObject
    ):
        return cls.construct_from(resp)

    else:
        return resp
