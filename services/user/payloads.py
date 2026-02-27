from faker import Faker
import random

faker = Faker()

class Payloads:

    def create_list_of_users_with_given_input_array(self):
        data = [{
                "id": random.randint(1, 100),
                "username": faker.user_name(),
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "email": faker.email(),
                "password": faker.password(),
                "phone": faker.phone_number(),
                "userStatus": random.randint(1, 100)
                }]
        return data

    def updated_user(self):
        data = {
                "id": random.randint(1, 100),
                "username": faker.user_name(),
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "email": faker.email(),
                "password": faker.password(),
                "phone": faker.phone_number(),
                "userStatus": random.randint(1, 100)
                }
        return data

    def logs_user_into_the_system(self):
        data = {"username": faker.user_name(),
                "password": faker.password()}
        return data

    def create_with_array(self):
        user_list = []
        for _ in range(3):
            data = {
                "id": random.randint(1, 100),
                "username": faker.user_name(),
                "firstName": faker.first_name(),
                "lastName": faker.last_name(),
                "email": faker.email(),
                "password": faker.password(),
                "phone": faker.phone_number(),
                "userStatus": random.randint(1, 100)
            }
            user_list.append(data)
        print(f"Сгенерировано пользователей: {len(user_list)}")
        return user_list


    def create_user_payload(self):
        data = {
            "id": random.randint(1, 100),
            "username": faker.user_name(),
            "firstName": faker.first_name(),
            "lastName": faker.last_name(),
            "email": faker.email(),
            "password": faker.password(),
            "phone": faker.phone_number(),
            "userStatus": random.randint(1, 100)
        }
        return data