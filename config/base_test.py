from services.pet.pet_api import PetApi
from services.store.store_api import StoreApi
from services.user.user_api import UserApi
from services.user.payloads import Payloads
class BaseTest:

    def setup_method(self):
        self.pet_api = PetApi()
        self.store_api = StoreApi()
        self.user_api = UserApi()
        self.payloads = Payloads()