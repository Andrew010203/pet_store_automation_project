from config.stages import get_stage

STAGE = get_stage()
HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    inventory = f"{HOST}/store/inventory"
    order = f"{HOST}/store/order"

    def find_order_by_id(self, order_id):
        return f"{HOST}/store/order/{order_id}"

    def delete_order_by_id(self, order_id):
        return f"{HOST}/store/order/{order_id}"
