<<<<<<< HEAD
# pet_store_automation_project
markdown
=======
>>>>>>> db3416a19f01f8e3a9cfc7423fbfc715f526c3dc
# 🐾 Petstore API Test Automation Framework

![Python](https://img.shields.io)
![Pytest](https://img.shields.io)
![Pydantic](https://img.shields.io)
![Allure](https://img.shields.io)

Профессиональный фреймворк для автоматизации тестирования REST API сервиса [Swagger Petstore](https://petstore.swagger.io). Проект демонстрирует реализацию архитектуры **Service Object** с модульной структурой сервисов.

---

## 🚀 Основные возможности

*   **Модульная архитектура:** Каждый сервис (User, Pet, Store) инкапсулирует свою логику, модели и генераторы данных.
<<<<<<< HEAD
*   **Schema Validation (Pydantic):** Строгая проверка структуры ответов API.
=======
*   **Schema Validation (Pydantic):** Строгая проверка структуры ответов API.
>>>>>>> db3416a19f01f8e3a9cfc7423fbfc715f526c3dc
*   **Data-Driven Testing:** Параметризация негативных сценариев через `pytest.mark.parametrize`.
*   **Динамические данные:** Использование `Faker` для генерации уникальных сущностей.
*   **Allure Reporting:** Наглядные отчеты с аттачами запросов и ответов.
*   **CI/CD Integration:** Автоматический запуск тестов в GitHub Actions.

---

>>>>>>> db3416a19f01f8e3a9cfc7423fbfc715f526c3dc
📊 Покрытые сценарии (Highlights)
User Service: Регистрация, авторизация (Session Flow), массовое создание, удаление с проверкой 404.
Pet Service: CRUD жизненный цикл питомца, фильтрация по статусам.
Store Service: Проверка инвентаря и корректность оформления заказов.
Negative Testing: Использование xfail для фиксации багов API (дубликаты, некорректные статусы ответа).
<<<<<<< HEAD

=======
>>>>>>> db3416a19f01f8e3a9cfc7423fbfc715f526c3dc
