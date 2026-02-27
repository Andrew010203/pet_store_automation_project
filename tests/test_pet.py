import allure
import pytest
from config.base_test import BaseTest

@allure.epic("Petstore")
@allure.feature("Pet")
class TestPet(BaseTest):

    @allure.title("Uploads an image")
    def test_uploads_an_image(self):
        pet_obj = self.pet_api.create_pet()
        self.pet_api.uploads_an_image(pet_obj.id)


    @allure.title("Add pet to the store")
    def test_create_pet(self):
        pet = self.pet_api.create_pet()

    @allure.title("Create pet with invalid data")
    @pytest.mark.parametrize("invalid_data, expected_status", [
        pytest.param({"name": "", "status": "available"}, 405, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 405, but got 200", strict=True)),  # Пустое имя
        pytest.param({"name": "Fido", "status": None}, 405, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 405, but got 200", strict=True)),  # Отсутствующий статус
        pytest.param({"invalid_field": "value"}, 405, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 405, but got 200", strict=True)),  # Некорректное поле
        pytest.param({"name": "Fido", "status": "available", "tags": [{"id": "not_a_number"}]}, 405, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 405, but got 500", strict=True)),  # Неправильный тип данных
        pytest.param("This is not a JSON", 400, marks=pytest.mark.xfail(
            reason="AssertionError: Expected 405, but got 500", strict=True))  # Совсем невалидный JSON(структурная ошибка)
    ])
    #pytest.param(..., marks=pytest.mark.xfail(reason="причина падения", strict=True # Упадет, если баг вдруг починят)) # используем данный способ для пометки падающих тестов
    def test_create_pet_invalid_data(self, invalid_data, expected_status):
        self.pet_api.create_pet_invalid_data(invalid_data, expected_status)



    @allure.title("Find pet by status")
    @pytest.mark.parametrize("status, expected_status", [
        ("available", 200),
        ("pending", 200),
        ("sold", 200),
        pytest.param("invalid_status", 400,
                     marks=pytest.mark.xfail(reason="Server returns 200 [] instead of 400 for invalid status", strict=True))
    ])
    def test_find_pet_by_status(self, status, expected_status):
        pets = self.pet_api.find_pet_by_status(status, expected_status)
        # Проверяем, что каждый питомец в списке имеет нужный статус
        if expected_status == 200:
            for pet in pets:
                assert pet.status == status, \
                    f"Фильтр сломан! Искали {status}, но нашли питомца ID:{pet.id} со статусом {pet.status}"

    @allure.title("Update an existing pet")
    def test_update_pet(self):
        self.pet_api.update_pet()


    @pytest.mark.parametrize("payload, expected_status", [
        # Кейс 1: Невалидный ID (строка вместо числа) — ожидаем 400 или 405 (в зависимости от реализации сервера)
        pytest.param({"id": "invalid_id", "name": "doggie"}, 400, marks=pytest.mark.xfail(reason="AssertionError: Expected 400, but got 500", strict=True)),

        # Кейс 2: Несуществующий ID — ожидаем 404
        pytest.param({"id": -1, "name": "ghost"}, 404, marks=pytest.mark.xfail(reason="AssertionError: Expected 404, but got 200", strict=True)),

        # Кейс 3: Отправка пустого тела запроса
        pytest.param({}, 405, marks=pytest.mark.xfail(reason="AssertionError: Expected 405, but got 200", strict=True))
    ])
    @allure.title("Update pet by id (negative)")
    def test_update_pet_by_id_negative(self, payload, expected_status):
        self.pet_api.update_pet_check_negative(payload, expected_status)

    # вариант с использованием фикстуры
    # @allure.title("Find pet by id")
    # def test_find_pet_by_id(self, new_pet, pet_api): # вариант использования фикстуры
    #     pet_api.find_pet_by_id(new_pet.id)

    @allure.title("Find pet by id")
    def test_find_pet_by_id(self):
        pet_obj = self.pet_api.create_pet()
        self.pet_api.find_pet_by_id(pet_obj.id)

    @pytest.mark.parametrize("pet_id, expected_status", [ #TODO негативные кейсы
        pytest.param(-1, 400, marks=pytest.mark.xfail(
            reason="Bug: Server returns 404 instead of 400 for negative IDs", strict=True)),
        pytest.param(99999999, 404, id="Non-existent id")
    ])
    @allure.title("Find pet by id (negative)")
    def test_find_pet_by_id_negative(self, pet_id, expected_status):
        self.pet_api.find_pet_by_id_negative(pet_id, expected_status)


    @allure.title("Updates a pet in the store with form data")
    def test_update_pet_by_id(self):
        pet_id = self.pet_api.create_pet()
        self.pet_api.update_pet_by_id(pet_id)


    @allure.title("Deletes a pet")
    def test_delete_pet(self):
        pet_obj = self.pet_api.create_pet()
        self.pet_api.delete_pet(pet_obj.id)

    @pytest.mark.parametrize("pet_id, expected_status", [
        pytest.param(0, 404, id="Delete non-existent pet"),
        pytest.param("abc", 404, id="Delete with invalid ID format")
    ])
    @allure.title("Deletes a pet (negative)")
    def test_delete_pet_negative(self, pet_id, expected_status):
        self.pet_api.delete_pet(pet_id, expected_status)



