from config.stages import get_stage

STAGE = get_stage()
HOST = "https://petstore.swagger.io/v2"
pet_id = None
class Endpoints:

    create_pet = f"{HOST}/pet"
    find_pet_by_status = f"{HOST}/pet/findByStatus"
    update_pet = f"{HOST}/pet"

    def upload_image(self, pet_id):
        return f"{HOST}/pet/{pet_id}/uploadImage"

    def find_pet_by_id(self, pet_id):
        return f"{HOST}/pet/{pet_id}"

    def update_pet_by_id(self, pet_id):
        return f"{HOST}/pet/{pet_id}"

    def delete_pet(self, pet_id):
        return f"{HOST}/pet/{pet_id}"




