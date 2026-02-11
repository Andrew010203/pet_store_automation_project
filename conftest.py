import os

import allure
from dotenv import load_dotenv
import requests
import pytest
from services.pet.pet_api import PetApi


# @pytest.fixture()
# def pet_api():
#     return PetApi()
#
# @pytest.fixture()
# def new_pet(pet_api):
#     """Создаёт питомца и возвращает объект модели PetResponse"""
#     # --- Setup: выполняем ПЕРЕД тестом ---
#     pet_data = pet_api.create_pet()
#     yield pet_data  # Передаем объект в тест
#     # --- Teardown: выполняется ПОСЛЕ теста ---
#     with allure.step(f"Cleanup: Delete pet with ID {pet_data.id}"):
#         pet_api.delete_pet(pet_data.id)
