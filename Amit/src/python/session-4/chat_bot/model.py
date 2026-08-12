import random
import json

with open("data.json", "r", encoding="utf-8") as file:
  responses = json.load(file)

def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])
