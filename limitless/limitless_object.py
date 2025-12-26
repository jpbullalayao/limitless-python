import json

class LimitlessObject(dict):
    def __init__(self, pk, api_token=None, **params):
        super(LimitlessObject, self).__init__()

        object.__setattr__(self, "api_token", api_token)

        if pk:
            pk_field = self.get_pk_field()
            self[pk_field] = pk

    def __setattr__(self, k, v):
        self[k] = v
        return None

    def __getattr__(self, k):
        return self[k]

    def _filter_internal_fields(self, obj):
        """Recursively filter out internal fields from dict/object structures."""
        if isinstance(obj, LimitlessObject):
            # Convert LimitlessObject to dict and filter
            result = {}
            for k, v in obj.items():
                if k != 'api_token':
                    result[k] = self._filter_internal_fields(v)
            return result
        elif isinstance(obj, dict):
            # Handle regular dicts
            result = {}
            for k, v in obj.items():
                if k != 'api_token':
                    result[k] = self._filter_internal_fields(v)
            return result
        elif isinstance(obj, list):
            # Handle lists
            return [self._filter_internal_fields(item) for item in obj]
        else:
            # Return primitive types as-is
            return obj

    def __repr__(self):
        """Pretty print using JSON format for REPL display."""
        filtered_data = self._filter_internal_fields(self)
        return json.dumps(filtered_data, indent=2, sort_keys=True)

    @classmethod
    def get_pk_field(cls):
        return cls.FIELD_PK

    @classmethod
    def construct_from(cls, resp):
        instance = cls(resp.get(cls.get_pk_field()))
        instance.refresh_from(resp)
        return instance

    def refresh_from(self, values):
        for k, v in iter(values.items()):
            super(LimitlessObject, self).__setitem__(k, v)
