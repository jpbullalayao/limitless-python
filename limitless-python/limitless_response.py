import json


class LimitlessResponse(object):
    def __init__(self, body):
        self.body = body
        self.data = json.loads(body)
