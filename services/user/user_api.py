import os

import allure
import requests
from helpers.helper import Helper
from services.user.endpoints import Endpoints
from services.user.models.model_create_with_list import WithListResponse
from services.user.models.model_get_user_by_username import GetUserByUsernameResponse
from services.user.models.model_logout import LogoutResponse
from services.user.models.model_logs_user_into_the_system import LogsUserIntoTheSystemResponse
from services.user.models.model_updated_user import UpdatedUserResponse
from services.user.payloads import Payloads
from config.headers import Headers



class UserApi(Helper):

    def __init__(self):
        self.endpoints = Endpoints()
        self.payloads = Payloads()
        self.headers = Headers()


    @allure.step("Creates list of users with given input array")
    def creates_list_of_users_with_given_input_array(self) -> WithListResponse:
        payload = self.payloads.create_list_of_users_with_given_input_array()
        response = requests.post(url=self.endpoints.with_list,
                                 headers=self.headers.user_header,
                                 json=payload)
        self.attach_response(response)
        self.validate_response(response, WithListResponse)
        print(f"Status: {response.status_code}")
        self.payloads.create_list_of_users_with_given_input_array()
        return payload[0].get("username")



    @allure.step("Get user by username")
    def get_user_by_username(self, username: str, expected_status=200) -> GetUserByUsernameResponse:
        response = requests.get(url=self.endpoints.user(username))
        self.attach_response(response)
        if expected_status == 200:
            self.validate_response(response, GetUserByUsernameResponse)
            print(response.json().get("username"))
        else:
            assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
        print(f"Status: {response.status_code}")




    @allure.step("Updated user")
    def updated_user(self, username: str) -> UpdatedUserResponse:
        payload = self.payloads.updated_user()
        response = requests.put(url=self.endpoints.updated_user(username),
                                json=payload)
        self.attach_response(response)
        self.validate_response(response, UpdatedUserResponse)
        print(f"Status: {response.status_code}")
        print(response.json())


    @allure.step("Updated user (negative)")
    def updated_user_negative(self, username, payload, expected_status):
        response = requests.put(url=self.endpoints.updated_user(username),
                                 headers=self.headers.basic,
                                 json=payload)
        print(response.status_code)
        self.attach_response(response)
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"


    @allure.step("Delete user")
    def delete_user(self, username: str):
        response = requests.delete(url=self.endpoints.delete_user(username))
        self.attach_response(response)
        self.validate_response(response, UpdatedUserResponse)
        print(f"Status: {response.status_code}")
        print(response.json())


    @allure.step("Logs user into the system")
    def logs_user_into_the_system(self):
        response = requests.get(url=self.endpoints.logs_user_into_the_system(),
                                headers=self.headers.get_user_into_the_system,
                                params=self.payloads.logs_user_into_the_system())
        self.attach_response(response)
        self.validate_response(response, LogsUserIntoTheSystemResponse)
        print(f"Status: {response.status_code}")
        print(response.json())
        session_number = response.json()['message'].split(':')[-1]
        print(session_number)
        return session_number

    @allure.step("Logs user into the system (negative)")
    def logs_user_into_the_system_negative(self, username, password, expected_status: int):
        response = requests.get(url=self.endpoints.logs_user_into_the_system(),
                                headers=self.headers.get_user_into_the_system,
                                params={"username": username, "password": password})
        self.attach_response(response)
        print(f"Status: {response.status_code}")
        print(response.json())
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"


    @allure.step("Logs out current logged in user session")
    def logs_out_current_logged_in_user_session(self, expected_status=200):
        response = requests.get(url=self.endpoints.logs_out_current_logged_in_user_session())
        self.attach_response(response)
        if expected_status == 200:
            self.validate_response(response, LogoutResponse)
        else:
            assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
        print(f"Status: {response.status_code}")
        print(response.json())


    @allure.step("Create list of users with given input array")
    def create_list_of_users_with_given_input_array(self, expected_status=200):
        response = requests.post(url=self.endpoints.create_list_with_array_url(),
                                headers=self.headers.user_header,
                                json=self.payloads.create_with_array())
        self.attach_response(response)
        self.validate_response(response, WithListResponse)
        print(f"Status: {response.status_code}")
        print(response.json())
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"


    @allure.step("Create user")
    def create_user(self, expected_status=200):
        payload = self.payloads.create_user_payload()
        response = requests.post(url=self.endpoints.create_user_url(),
                                headers=self.headers.user_header,
                                json=payload)
        self.attach_response(response)
        self.validate_response(response, UpdatedUserResponse)
        print(f"Status: {response.status_code}")
        print(response.json())
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
        username = payload.get("username")
        return username


    @allure.step("Create user (negative)")
    def create_user_negative(self, payload, expected_status: int):
        response = requests.post(url=self.endpoints.create_user_url(),
                                headers=self.headers.user_header,
                                json=payload)
        self.attach_response(response)
        print(f"Status: {response.status_code}")
        print(response.json())
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"


