import os
from dotenv import load_dotenv

load_dotenv()
class Headers:
    basic = {
        "api_key": "special-key",
        'Content-Type': 'application/json'
    }

    fill_file = {
        "api_key": "special-key",
        # 'Content-Type': 'multipart/form-data'
    }

    store_header = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    user_header = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    get_user_into_the_system = {
        'accept': 'application/json'
    }
