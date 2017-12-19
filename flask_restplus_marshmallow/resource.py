from flask_restplus import Resource as OriginalResource


class Resource(OriginalResource):

    @classmethod
    def _apply_decorator_to_methods(cls, decorator):
        """
        This helper can apply a given decorator to all methods on the current
        Resource.
        NOTE: In contrast to ``Resource.method_decorators``, which has a
        similar use-case, this method applies decorators directly and override
        methods in-place, while the decorators listed in
        ``Resource.method_decorators`` are applied on every request which is
        quite a waste of resources.
        """
        for method in cls.methods:
            method_name = method.lower()
            decorated_method_func = decorator(getattr(cls, method_name))
            setattr(cls, method_name, decorated_method_func)
