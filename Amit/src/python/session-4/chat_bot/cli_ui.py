from model import get_response


def main_bot():
  print("Chatbot: Hi how i can help you?")
  while True:
    user_input = input("User:     ").lower()

    if user_input == "goodbye":
      print("Chatbot : Goodbye!")
      break

    response = get_response(user_input)
    print("Chatbot : ", response)