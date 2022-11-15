#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Places """
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/cities/<city_id>/places', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/place/get_places.yml', methods=['GET'])
def get_places(city_id):
    """
    Retrieves the list of all Place objects of a City
    """
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    places = [place.to_dict() for place in city.places]

    return jsonify(places)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/place/get_place.yml', methods=['GET'])
def get_place(place_id):
    """
    Retrieves a Place object
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/place/delete_place.yml', methods=['DELETE'])
def delete_place(place_id):
    """
    Deletes a Place Object
    """

    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    storage.delete(place)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/place/post_place.yml', methods=['POST'])
def post_place(city_id):
    """
    Creates a Place
    """
    city = storage.get(City, city_id)

    if not city:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])

    if not user:
        abort(404)

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data["city_id"] = city_id
    instance = Place(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/place/put_place.yml', methods=['PUT'])
def put_place(place_id):
    """
    Updates a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)


def add_reviews(place):
    """adds the reviews attribute to a place

    Args:
        place (Place object): the place to add reviews to
    """
    reviews = [review.__dict__ for review in place.reviews]
    return {'reviews': reviews} | place.to_dict()


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
@swag_from('documentation/place/post_search.yml', methods=['POST'])
def places_search():
    """
    Retrieves all Place objects depending of the JSON in the body
    of the request
    """

    if request.get_json() is None:
        abort(400, description="Not a JSON")

    data = request.get_json()
    all_places = storage.all(Place).values()
    state_places = []
    city_places = []
    amenity_places = []

    amenities = data.get('amenities', [])
    states = data.get('states', [])
    cities = data.get('cities', [])

    con = [not len(amenities), not len(states), not len(cities)]
    if not len(data) or all(con):
        return [add_reviews(place) for place in all_places]

    if len(states):
        for place in all_places:
            if storage.all()[f'City.{place.city_id}'].state_id in states:
                state_places.append(place)

        if len(data) == 1:
            return [add_reviews(place) for place in state_places]

    if len(cities):
        for place in all_places:
            if storage.all()[f'City.{place.city_id}'].id in cities:
                city_places.append(place)

        if len(data) == 1:
            return [add_reviews(place) for place in city_places]

    if len(amenities):
        for place in all_places:
            # if place has all amenities
            if set(amenities).issubset(set(place.amenity_ids)):
                amenity_places.append(place)

        if len(data) == 1 or (not len(states) and not len(cities)):
            return [add_reviews(place) for place in amenity_places]

        # filter states and cities amenities
        else:
            combined_places = state_places + city_places
            filtered_list = []
            for place in combined_places:
                # if place has all amenities
                if set(amenities).issubset(set(place.amenity_ids)):
                    filtered_list.append(add_reviews(place))
            return filtered_list

    # remove duplicate places
    combined_places = state_places + city_places
    combined_places = list(set(combined_places))
    return [add_reviews(place) for place in combined_places]
