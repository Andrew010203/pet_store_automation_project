import allure
import requests
from helpers.helper import Helper
from services.store.endpoints import Endpoints
from services.store.models.model_find_order_by_id import FindOrderByIdResponse
from services.store.models.model_inventory import InventoryResponse
from services.store.models.model_order import OrderResponse
from services.store.payloads import Payloads
from config.headers import Headers


class StoreApi(Helper):

    def __init__(self):
        self.endpoints = Endpoints()
        self.payloads = Payloads()
        self.headers = Headers()

    @allure.step("Returns pet inventories by status")
    def returns_pet_inventories_by_status(self):
        response = requests.get(url=self.endpoints.inventory)
        self.attach_response(response.json())
        self.validate_response(response, InventoryResponse)
        print(f"Status: {response.status_code}")


    @allure.step("Place an order for a pet")
    def place_an_order_for_a_pet(self):
        response = requests.post(url=self.endpoints.order,
                                 headers=self.headers.store_header,
                                 json=self.payloads.order_pet())
        self.attach_response(response)
        data = self.validate_response(response, OrderResponse)
        print(f"Status: {response.status_code}")
        print(response.json())
        return(data.id)

    @allure.step("Place an order for a pet (negative)")
    def place_an_order_invalid_data(self, invalid_data, expected_status):
        response = requests.post(url=self.endpoints.order,
                                 headers=self.headers.store_header,
                                 json=invalid_data)
        print(response.status_code)
        self.attach_response(response)
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"

    @allure.step("Find purchase order by id")
    def find_purchase_order_by_id(self, order_id: int, expected_status):
        url = self.endpoints.find_order_by_id(order_id)
        response = requests.get(url=url, headers=self.headers.store_header)
        self.attach_response(response)
        print(f"Status: {response.status_code}")
        print(response.json())
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
        if response.status_code == 200:
            data = self.validate_response(response, FindOrderByIdResponse)
            return data.id


    @allure.step("Delete purchase order by id")
    def delete_purchase_order_by_id(self, order_id: int, expected_status):
        url = self.endpoints.delete_order_by_id(order_id)
        response = requests.delete(url=url, headers=self.headers.store_header)
        self.attach_response(response)
        print(f"Status: {response.status_code}")
        print(response.json())
        assert response.status_code == expected_status, f"Expected {expected_status}, but got {response.status_code}"
