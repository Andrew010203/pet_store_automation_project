import random
import allure
import requests
from helpers.helper import Helper
from services.pet.endpoints import Endpoints
from services.pet.models.model_add_pet import PetResponse
from services.pet.models.model_find_by_status import PetResponseFindByStatus
from services.pet.models.model_find_pet_by_id import PetResponseFindById
from services.pet.models.model_update_pet_by_id import PetResponseUpdateById
from services.pet.models.model_upload_image import ResponseImageModel
from services.pet.payloads import Payloads
from config.headers import Headers


class PetApi(Helper):
    def __init__(self):
        self.endpoints = Endpoints()
        self.payloads = Payloads()
        self.headers = Headers()


    @allure.step("Uploads an image")
    def uploads_an_image(self, pet_id: int) -> ResponseImageModel:
        response = requests.post(url=self.endpoints.upload_image(pet_id),
                                 headers=self.headers.fill_file, files=self.payloads.add_image())
        self.attach_response(response.json())
        self.validate_response(response, ResponseImageModel)
        print(f"Status: {response.status_code}")
        print(response.json())


    @allure.step("Create pet")
    def create_pet(self) -> PetResponse:
        response = requests.post(url=self.endpoints.create_pet,
                                 headers=self.headers.basic,
                                 json=self.payloads.create_pet())
        self.attach_response(response.json())
        self.validate_response(response, PetResponse)
        print(f"Status: {response.status_code}")
        print(response.json())
        return self.validate_response(response, PetResponse)


    @allure.step("Create pet with invalid data")
    def create_pet_invalid_data(self, invalid_data, expected_status):
        response = requests.post(url=self.endpoints.create_pet,
                                 headers=self.headers.basic,
                                 json=invalid_data)
        print(response.status_code)
        self.attach_response(response.json())
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
        # assert response.status_code == expected_status
        # Дополнительно: можно проверить, что response.json() содержит сообщение об ошибке


    @allure.step("Find pet by status")
    def find_pet_by_status(self, status: str, expected_status: int) -> list[PetResponseFindByStatus]:
        response = requests.get(url=self.endpoints.find_pet_by_status,
                                headers=self.headers.basic,
                                params={"status": status})
        self.attach_response(response.json())
        print(f"Status: {response.status_code}")
        print(response.json())
        return self.validate_response(response, PetResponseFindByStatus, status_code=expected_status)


    @allure.step("Update an existing pet")
    def update_pet(self) -> PetResponse:
        response = requests.put(url=self.endpoints.update_pet,
                                headers=self.headers.basic,
                                json=self.payloads.put_pet())
        self.attach_response(response.json())
        self.validate_response(response, PetResponse)
        print(f"Status: {response.status_code}")
        print(response.json())


    @allure.step("Update an existing pet with custom payload")
    def update_pet_check_negative(self, payload: dict, expected_status: int = 200):
        """Негативные сценарии"""
        response = requests.put(url=self.endpoints.update_pet,
                                headers=self.headers.basic,
                                json=payload)
        self.attach_response(response.json())
        print(response.text)
        print(f"Status: {response.status_code}")
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"


    @allure.step("Find pet by id")
    def find_pet_by_id(self, pet_id: int) -> PetResponseFindById:
        response = requests.get(url=self.endpoints.find_pet_by_id(pet_id))
        self.attach_response(response.json())
        self.validate_response(response, PetResponseFindById)
        print(f"Status: {response.status_code}")
        print(response.json())


    @allure.step("Find pet by id (negative)")
    def find_pet_by_id_negative(self, pet_id: int, expected_status: int):
        response = requests.get(url=self.endpoints.find_pet_by_id(pet_id))
        print(f"Status: {response.status_code}")
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
        self.attach_response(response.text)
        return response


    @allure.step("Updates a pet in the store with form data")
    def update_pet_by_id(self, pet_id: int, name: str = None, status: str = None) -> PetResponseUpdateById:
        # TODO решить вопрос с корректностью ответа от сервера(приходит XML)
        data = {}
        if name:
            data['name'] = name
        if status:
            data['status'] = status
        response = requests.post(url=self.endpoints.update_pet_by_id(pet_id))
        print(f"Status: {response.status_code}")
        self.attach_response(response.text)
        return response


    @allure.step("Deletes a pet")
    def delete_pet(self, pet_id: int, expected_status: int = 200):
        response = requests.delete(url=self.endpoints.delete_pet(pet_id))
        self.attach_response(response.text)
        # self.validate_response(response, PetResponseFindById)
        print(f"Status: {response.status_code}")
        print(response.text)
        assert response.status_code == expected_status, \
            f"Expected {expected_status}, but got {response.status_code}"