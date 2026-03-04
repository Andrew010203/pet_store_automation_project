# pet_store_automation_project
markdown
# 🐾 Petstore API Test Automation Framework

![Python](https://img.shields.io)
![Pytest](https://img.shields.io)
![Pydantic](https://img.shields.io)
![Allure](https://img.shields.io)

Профессиональный фреймворк для автоматизации тестирования REST API сервиса [Swagger Petstore](https://petstore.swagger.io). Проект демонстрирует реализацию архитектуры **Service Object** с модульной структурой сервисов.

---

## 🚀 Основные возможности

*   **Модульная архитектура:** Каждый сервис (User, Pet, Store) инкапсулирует свою логику, модели и генераторы данных.
*   **Schema Validation (Pydantic):** Строгая проверка структуры ответов API.
*   **Data-Driven Testing:** Параметризация негативных сценариев через `pytest.mark.parametrize`.
*   **Динамические данные:** Использование `Faker` для генерации уникальных сущностей.
*   **Allure Reporting:** Наглядные отчеты с аттачами запросов и ответов.
*   **CI/CD Integration:** Автоматический запуск тестов в GitHub Actions.

---
🛠 Технологический стек
Language: Python 3.12+
Tests: Pytest
HTTP: Requests
Validation: Pydantic V2
Data: Faker
Report: Allure

📊 Покрытые сценарии (Highlights)
User Service: Регистрация, авторизация (Session Flow), массовое создание, удаление с проверкой 404.
Pet Service: CRUD жизненный цикл питомца, фильтрация по статусам.
Store Service: Проверка инвентаря и корректность оформления заказов.
Negative Testing: Использование xfail для фиксации багов API (дубликаты, некорректные статусы ответа).

