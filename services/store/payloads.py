from faker import Faker
import random

faker = Faker()

class Payloads:

    def order_pet(self):
        return {
              "id": random.randint(1, 100),
              "petId": random.randint(1, 100),
              "quantity": random.randint(1, 100),
              "shipDate": "2026-02-18T09:29:57.263Z",
              "status": "placed",
              "complete": True
            }