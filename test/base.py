from api.api import get_keyword_by_id, get_person_by_id, get_movie_by_id, post_movie_rating, delete_movie_rating
from constants import API_KEY


class TestBase:
    def get_movie_by_id(self, status_code=None, movie_id=False, language=None, append_to_response=None):
#        if movie_id is False:
#            movie_id = self.movie_id
#        if language is False:
#            language = self.language
#        if append_to_response is False:
#            append_to_response = self.append_to_response
            
        response_get = get_movie_by_id(
            movie_id=movie_id,
            language=language,
            append_to_response=append_to_response
        )
        if not status_code is None:
            assert (
                    response_get.status_code == status_code
            ), f"response's status code is {response_get.status_code}, it should be {status_code}"
            return response_get.json()
        return response_get

    def get_person_by_id(self, status_code=None, person_id=False, language=None, append_to_response=None):
        response_get = get_person_by_id(
            person_id=person_id,
            language=language,
            append_to_response=append_to_response
        )
        if not status_code is None:
            assert (
                response_get.status_code == status_code
            ), f"response's status code is {response_get.status_code}, it should be {status_code}"
            return response_get.json()
        return response_get

    def post_movie_rating(self, status_code=None, movie_id=False, guest_session_id=False, rate=False):
        if movie_id is False:
            movie_id = self.movie_id
        if guest_session_id is False:
            guest_session_id = self.guest_session_id
        response_post = post_movie_rating(
            movie_id=movie_id,
            guest_session_id=guest_session_id,
            rate=rate
        )
        if not status_code is None:
            assert (
                    response_post.status_code == status_code
            ), f"response's status code is {response_post.status_code}, it should be {status_code}"
        return response_post.json()

    def delete_movie_rating(self, status_code=None, movie_id=False, guest_session_id=False):
        if movie_id is False:
            movie_id = self.movie_id
        if guest_session_id is False:
            guest_session_id = self.guest_session_id
        response_delete = delete_movie_rating(
            movie_id=movie_id,
            guest_session_id=guest_session_id
        )
        if not status_code is None:
            assert (
                    response_delete.status_code == status_code
            ), f"response's status code is {response_delete.status_code}, it should be {status_code}"
            return response_delete.json()
        return response_delete
    
    def get_keywords_by_id(self, api_key=API_KEY, status_code=None, movie_id=False, guest_session_id=False):
        response_get_keyword_by_id = get_keyword_by_id(
            movie_id=movie_id,
            api_key=api_key
        )

        if not status_code is None:
            assert(
                response_get_keyword_by_id == status_code
            ), f"response's status code is {response_get_keyword_by_id.status_code}, it should be {status_code}"
            return response_get_keyword_by_id.json()
        return response_get_keyword_by_id

    def assert_check_type(self, obj_property, obj_property_type):
        assert type(obj_property) == obj_property_type

