import allure
import pytest
from config.base_test import BaseTest

@allure.epic("Petstore")
@allure.feature("Store")
class TestStore(BaseTest):

    @allure.title("Returns pet inventories by status")
    def test_inventory(self):
        self.store_api.returns_pet_inventories_by_status()


    @allure.title("Place an order for a pet")
    def test_order(self):
        self.store_api.place_an_order_for_a_pet()


    @allure.title("Place an order for a pet (negative)")
    @pytest.mark.parametrize("invalid_data, expected_status", [
        pytest.param({"id": "abc"}, 400, id="string_instead_of_int", marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 500", strict=True)),
        pytest.param({"quantity": -1}, 400, id="negative_quantity", marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 200", strict=True)),
        pytest.param({}, 400, id="empty_body", marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 200", strict=True)),
        pytest.param({"shipDate": "invalid-date"}, 400, id="invalid_date_format", marks=pytest.mark.xfail(
            reason="AssertionError: Expected 400, but got 500", strict=True))
    ])
    def test_place_an_order_invalid_data(self, invalid_data, expected_status):
        self.store_api.place_an_order_invalid_data(invalid_data, expected_status)


    @allure.title("E2E create order, get order by id, delete order by id")
    def test_create_order_get_order_delete_order(self):
        id = self.store_api.place_an_order_for_a_pet()
        self.store_api.find_purchase_order_by_id(id, expected_status=200)
        self.store_api.delete_purchase_order_by_id(id, expected_status=200)
        self.store_api.find_purchase_order_by_id(id, expected_status=404)