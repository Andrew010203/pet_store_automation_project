import os

stage = "https://petstore.swagger.io/v2"

def get_stage():
    stage_key = os.getenv("STAGE")
    # return stages[stage_key]
    return stage