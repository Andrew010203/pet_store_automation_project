import allure
import requests
import pytest
from config.base_test import BaseTest
from services.user.payloads import Payloads


@allure.epic("Petstore")
@allure.feature("User")
class TestUser(BaseTest):

    @allure.title("Creates list of users with given input array")
    def test_creates_list_of_users_with_given_input_array(self):
        self.user_api.creates_list_of_users_with_given_input_array()

    @allure.title("Get user by username")
    def test_get_user_by_username(self):
        username = self.user_api.creates_list_of_users_with_given_input_array()
        print(username)
        self.user_api.get_user_by_username(username)

    @allure.title("Updated user")
    def test_updated_user(self):
        username = self.user_api.creates_list_of_users_with_given_input_array()
        print(username)
        self.user_api.updated_user(username)


    @allure.title("Updated user (negative)")
    @pytest.mark.parametrize("username, payload, expected_status", [
            pytest.param("non_existent_user", {"id": 1, "username": "new"}, 404, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 404, but got 200", strict=True)),  # Несуществующий пользователь
            pytest.param("valid_user", {"id": "invalid_type"}, 400, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 500", strict=True)),  # Неправильный тип id,
            pytest.param("invalid_id", {"id": -1}, 400, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 200", strict=True)),  # Отрицательный id
            pytest.param("invalid_json", {}, 400, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 200", strict=True)),  # Пустой json
            pytest.param("invalid_json", {"email": "qwerty123.com"}, 400, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 200", strict=True))  # Неправильный email
    ])
    def test_updated_user_negative(self, username, payload, expected_status):
        self.user_api.updated_user_negative(username, payload, expected_status)


    @allure.title("Delete user")
    def test_delete_user(self):
        username = self.user_api.creates_list_of_users_with_given_input_array()
        print(username)
        self.user_api.delete_user(username)
        self.user_api.get_user_by_username(username, expected_status=404)


    @allure.title("Logs user into the system")
    def test_logs_user_into_the_system(self):
        self.user_api.logs_user_into_the_system()


    @allure.title("Logs user into the system (negative)")
    @pytest.mark.parametrize("username, password, expected_status", [
        pytest.param("non_existent_password", "new123qwe", 404, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 404, but got 200", strict=True)),
        pytest.param("empty_data", "", 404, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 404, but got 200", strict=True)),
        pytest.param("non_existent_user", "qwezxc", 404, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 404, but got 200", strict=True)),
    ])
    def test_logs_user_into_the_system_negative(self, username, password, expected_status):
        self.user_api.logs_user_into_the_system_negative(username, password, expected_status)


    @allure.title("Logout without login (expected fail)")
    @pytest.mark.xfail(reason="API returns 200 instead of 401/404", strict=True)
    def test_logs_out_current_logged_in_user_session(self):
        self.user_api.logs_out_current_logged_in_user_session(expected_status=401)

    @allure.title("Full Login-Logout flow")
    def test_login_logout_flow(self):
        self.user_api.logs_user_into_the_system()
        self.user_api.logs_out_current_logged_in_user_session(expected_status=200)

    @allure.title("Create list of users with given input array")
    def test_create_list_of_users_with_given_input_array(self):
        self.user_api.create_list_of_users_with_given_input_array()


    @allure.title("Create user")
    def test_create_user(self):
        username = self.user_api.create_user()
        self.user_api.get_user_by_username(username)


    @allure.title("Create user (negative)")
    @pytest.mark.parametrize("payload, info, expected_status", [
        pytest.param({}, 400, "empty_body", marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 200", strict=True)),
        pytest.param({"id": "abc"}, 400, "invalid_type_id", marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 200", strict=True))
    ])
    def test_create_user_negative(self, payload, info, expected_status):
        self.user_api.create_user_negative()

    @allure.title("Create duplicate user")
    @pytest.mark.xfail(reason="Petstore allows duplicate usernames", strict=True)
    def test_create_duplicate_user(self):
        payload = self.payloads.create_user_payload()
        self.user_api.create_user_negative(payload, expected_status=200)
        self.user_api.create_user_negative(payload, expected_status=409)







