from config.stages import get_stage

STAGE = get_stage()
HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    with_list = f"{HOST}/user/createWithList"


    def user(self, username):
        return f"{HOST}/user/{username}"


    def updated_user(self, username):
        return f"{HOST}/user/{username}"

    def delete_user(self, username):
        return f"{HOST}/user/{username}"

    def logs_user_into_the_system(self):
        return f"{HOST}/user/login"


    def logs_out_current_logged_in_user_session(self):
        return f"{HOST}/user/logout"

    def create_list_with_array_url(self):
        return f"{HOST}/user/createWithArray"

    def create_user_url(self):
        return f"{HOST}/user"
