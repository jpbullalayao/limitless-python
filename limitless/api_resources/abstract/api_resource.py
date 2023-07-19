from limitless.limitless_object import LimitlessObject

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
