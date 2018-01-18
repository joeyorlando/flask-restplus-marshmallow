from six import itervalues
from flask_marshmallow import Schema


class Parameters(Schema):

    LOCATION = 'json'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in itervalues(self.fields):
            if field.dump_only:
                continue
            if not field.metadata.get('location'):
                field.metadata['location'] = self.LOCATION

class JSONParameters(Parameters):

    LOCATION = 'json'

class QueryParameters(Schema):

    LOCATION = 'query'
