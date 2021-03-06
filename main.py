from flask_restful import  Api
from src.apps import app
from src.views import PersonView, PersonListView

api = Api(app)
api.add_resource(PersonView, '/person/<person_id>')
api.add_resource(PersonListView, '/person')

# Start the flask loop
if __name__ == '__main__':
    app.run()

