from .base import TestBase
import pytest
import sys


class TestGetMethod(TestBase):
    @pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python 3.7 or higher")
    def test_get_status_code_movie(self):
        # When the movie data is retrieved
        response = self.get_movie_by_id(
            movie_id="500"
        )
        # Then the response should have the proper status code
        assert (
            response.status_code == 200
        ), "The response should contain status code 200"

    def test_get_status_code_person(self):
        response = self.get_person_by_id(
            person_id="72466"
        )
        assert (
            response.status_code == 200
        ), "The response should contain status code 200"

    @pytest.mark.parametrize(
        # argnames
        # A comma-separated string denoting one or more argument names, or a list/tuple of argument strings.
        "movie_id, title",

        # argvalues
        # If N argnames were specified, argvalues must be a list of N-tuples, where each tuple-element specifies a value for its respective argname.
        [
            ("335983", "Venom"),
            ("577922", "Tenet"),
            ("420818", "The Lion King")
        ]
    )
    def test_get_response_title(self, movie_id, title):
        # When the movie data is retrieved
        response = self.get_movie_by_id(
            status_code=200,
            movie_id=movie_id
        )
        # Then the title should be equal to the title that belongs to the ID
        assert (
            response["title"] == title
        ), f"The '{movie_id}' ID should have the '{title}' title"

    @pytest.mark.parametrize(
        "person_id, name",
        [
            ("72466", "Colin Farrell"),
            ("6384", "Keanu Reeves"),
            ("54693", "Emma Stone"),
            pytest.param("23356", "Kata Dobó", marks=pytest.mark.xfail)
        ]
    )
    def test_get_response_name(self, person_id, name):
        response = self.get_person_by_id(
            status_code=200,
            person_id=person_id
        )
        assert (
            response["name"] == name
        ), f"The '{person_id}' ID should have the '{name}' title"

    def test_get_without_param(self):
        # When the movie id is not added to the parameters
        response = self.get_movie_by_id(
            movie_id=None
        )
        # Then the response should have the proper status code
        assert (
            response.status_code == 404
        ), "The response should contain status code 404"

    @pytest.mark.parametrize(
        "movie_id",
        ["335983", "577922", "420818"]
    )
    def test_get_keywords(self, movie_id):
        response = self.get_keywords_by_id(
            movie_id=movie_id
        )

        response = response.json()

        assert 'keywords' in response
        for obj in response['keywords']:
            assert 'id' in obj
            assert 'name' in obj
            self.assert_check_type(obj['id'], int)
            self.assert_check_type(obj['name'], str)

    def test_get_keywords_invalid(self):
        response = self.get_keywords_by_id(
            movie_id="335983",
            api_key=False
        )

        assert (response.status_code ==
                401), "The response should contain status code 401"
        assert response.json()[
            'status_message'] == "Invalid API key: You must be granted a valid key."
