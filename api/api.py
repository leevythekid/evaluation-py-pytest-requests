import requests
from constants import API_KEY_STRING, API_KEY, API_URL, KEY


def get_movie_by_id(movie_id, language, append_to_response):
    url = f"{API_URL}/movie/{movie_id}{KEY}"
    params = {}
    if movie_id is not None:
        params["movie_id"] = movie_id

    if language is not None:
        params["language"] = language

    if append_to_response is not None:
        params["append_to_response"] = append_to_response

    return requests.get(url=url, params=params)


def post_movie_rating(movie_id, rate, guest_session_id):
    url = f"{API_URL}/movie/{movie_id}/rating{KEY}"
    params = {}
    if guest_session_id is not None:
        params["guest_session_id"] = guest_session_id

    return requests.post(url=url, params=params, json=rate)


def delete_movie_rating(movie_id, guest_session_id):
    url = f"{API_URL}/movie/{movie_id}/rating{KEY}"
    params = {}
    if guest_session_id is not None:
        params["guest_session_id"] = guest_session_id

    return requests.delete(url=url, params=params)


def get_person_by_id(person_id, language, append_to_response):
    url = f"{API_URL}/person/{person_id}{KEY}"
    params = {}
    if person_id is not None:
        params["person_id"] = person_id
    
    if language is not None:
        params["language"] = language

    if append_to_response is not None:
        params["append_to_response"] = append_to_response

    return requests.get(url=url, params=params)


def get_keyword_by_id(movie_id, api_key=API_KEY):
    url = f"{API_URL}/movie/{movie_id}/keywords{API_KEY_STRING}{api_key}"

    return requests.get(url)