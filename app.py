from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import re
from itn import evaluate

app = Flask(__name__)
api = Api(app)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


class TranslateText(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()

        user_query = args['query']

        if user_query != None:
            # inputText = []
            inputText=user_query

            # vectorize the user's query and make a prediction
            outText = evaluate(inputText)
            print(outText)

            # create JSON object
            output = {'Normalized Text': outText}
            return output
        return {'normalized Text': ''}


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(TranslateText, '/')

if __name__ == '__main__':
    app.run(port=5002, debug=True)