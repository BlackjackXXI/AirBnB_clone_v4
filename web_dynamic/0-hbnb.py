#!/usr/bin/python3
"""
Web Application interfacing with AirBnB HTML Template
"""
from flask import Flask, render_template, url_for
from models import storage
import uuid

# configuring Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# ending flask page rendering
@app.teardown_appcontext
def close_db(exception):
    """
    Removes the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/0-hbnb')
def hbnb(id=None):
    """
    Serves custom template with states, cities, and amenities
    """
    state_objs = storage.all('State').values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all('Amenity').values()
    places = storage.all('Place').values()
    users = dict([user.id, "{} {}".format(user.first_name, user.last_name)]
                 for user in storage.all('User').values())
    cache_id = uuid.uuid4()
    return render_template('0-hbnb.html',
                           states=states,
                           amens=amens,
                           places=places,
                           users=users,
                           cache_id=cache_id)

if __name__ == "__main__":
    """
    Main Flask Application
    """
    app.run(port=port, host=host)
