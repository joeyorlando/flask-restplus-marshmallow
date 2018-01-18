from six import itervalues
from flask_marshmallow import Schema


class JSONParameters(Schema):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.location = 'json'

        for field in itervalues(self.fields):
            if field.dump_only:
                continue
            if not field.metadata.get('location'):
                field.metadata['location'] = 'json'

class QueryParameters(Schema):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.location = 'query'

        for field in itervalues(self.fields):
            if field.dump_only:
                continue
            if not field.metadata.get('location'):
                field.metadata['location'] = 'query'
