# Flask RESTPlus + Marshmallow


## Synposis
This library serves as an amalgamation between [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/) and [Marshmallow](https://marshmallow.readthedocs.io/en/3.0/), allowing you to use Marshmallow schemas to define Swagger API schema, as well as handle request validation and response marshalling.

## Rationale

This project was spawned as a fork from [frol](https://github.com/frol)'s (maintainer of Flask-RESTPlus) Flask-RestPLUS fork, which added Marshmallow schema functionality, which in turn spawned from [this](https://github.com/noirbizarre/flask-restplus/issues/9#issuecomment-422555888) issue thread in the Flask-RESTPlus project. This project slightly modifies the parent fork, augmenting with MIT specific features.

## Example Code
```python
from flask import Flask, Blueprint
from flask_restplus_marshmallow import abort, Api, Schema, Resource, Namespace, JSONParameters
from marshmallow import fields
from pony.orm import db_session
import typing

app = Flask(__name__)
blueprint = Blueprint('my-api', __name__)
api = Api(
  blueprint,
  title='My REST API',
  version='1.0',
  description='My super helpful description for my REST API'
)


auth_ns = Namespace(
  name='authentication',
  description='My authentication related routes',
  path="/authentication",
  db_context=db_session
)

class AuthenticationRequestSchema(JSONParameters):

  password = fields.String(required=True)
  email = fields.Email(required=True)

class AuthenticationSuccessfulResponseSchema(Schema):

  user = fields.Nested('MyUserSchema')
  token = fields.String()

@auth_ns.route("/login")
class LoginRoutes(Resource):
  
  @auth_ns.parameters(AuthenticationRequestSchema())
  @auth_ns.response(code=401)
  @auth_ns.response(AuthenticationSuccessfulResponseSchema())
  def post(self, data: typing.Dict) -> typing.Dict:
    successfully_authenticated = ... # some authentication related business logic here
    if successfully_authenticated:
      return {
        "user": {}, # JSON response here
        "token": "foo_bar_baz"
      }
    return abort(401)


api.add_namespace(auth_ns)
```

## Extended Documentation
- [`Api` class](https://flask-restplus.readthedocs.io/en/stable/api.html#flask_restplus.Api)
- [`Resource` class](https://flask-restplus.readthedocs.io/en/stable/api.html#flask_restplus.Resource)
- [`Namespace` class](https://flask-restplus.readthedocs.io/en/stable/api.html#flask_restplus.Namespace)
- [`abort` helper method](https://flask-restplus.readthedocs.io/en/stable/api.html#flask_restplus.Namespace.abort)
- [`Schema` class](https://marshmallow.readthedocs.io/en/latest/api_reference.html#marshmallow.Schema)
- [`fields` schema related module](https://marshmallow.readthedocs.io/en/latest/api_reference.html#module-marshmallow.fields)

## Contributions
Contributions are welcome! Simply create a feature branch off of `master` and open a pull request. This project is maintained by the Motional Internal Tools team whom can be reached on Slack at `#motion-internal-tools`.

## Roadmap
- Remove dependency on Pony ORM `db_session`, allow this to be optional

## Useful links
- [Parent fork documentation](https://github.com/frol/flask-restplus-server-example)
- [Flask-RESTPlus documentation](https://flask-restplus.readthedocs.io/en/stable/)
- [Marshmallow documentation](https://marshmallow.readthedocs.io/en/3.0/)