from flask_restplus import Api as OriginalApi
from werkzeug import cached_property
from .swagger import Swagger


class Api(OriginalApi):

    @cached_property
    def __schema__(self):
        # The only purpose of this method is to pass custom Swagger class
        return Swagger(self).as_dict()
