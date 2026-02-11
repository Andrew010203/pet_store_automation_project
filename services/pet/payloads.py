from faker import Faker
import random

faker = Faker()

class Payloads:

    def create_pet(self):
        return {
          "id": random.randint(1, 100),
          "category": {
            "id": random.randint(1, 100),
            "name": faker.file_name()
          },
          "name": faker.name(),
          "photoUrls": [
            faker.url()
          ],
          "tags": [
            {
              "id": random.randint(1, 100),
              "name": faker.user_name()
            }
          ],
          "status": "available"
        }



    def put_pet(self, **kwargs):
        payload = {
          "id": random.randint(1000, 9000),
          "category": {
            "id": random.randint(1, 100),
            "name": faker.file_name()
          },
          "name": faker.name(),
          "photoUrls": [
            faker.url()
          ],
          "tags": [
            {
              "id": random.randint(1, 100),
              "name": faker.user_name()
            }
          ],
          "status": "available"
        }
        payload.update(kwargs)  # Перезаписываем поля, переданные в тест
        return payload

    def add_image(self):
      files = {
        'file': ("MeM.jpg", open("MeM.jpg", "rb"), 'image/jpeg')
      }
      return files

    def pet_update_by_id(self):
      data = {
        'name': faker.name(),
        'status': 'available'
      }
      return data