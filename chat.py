from retailchatbot import RetailChatBot

"""Chatbot with below Flow Diagram - Rule Based Chatbot

        1. Start
        2. Chatbot introduction/Welcome message.
        3. Enter the while loop for user interaction.
        4. User input is received.
        5. If the user input contains 'order', go to step 6. Otherwise, go to step 8.
        6. Input should have at least three parts, order [item] [quantity]. If not, ask user to correct input format. If exception (non-integer quantity or invalid item), ask for re-input and go to step 4.
        7. If quantity of item is sufficient, place order and calculate total cost, then ask if user wants to order something else. If not sufficient, inform user and ask for new order. Go back to step 3.
        8. Chatbot responds to other functions like inquiries about price or stock, greetings, help, and unrecognized commands.
        9. If user inputs "goodbye", break the loop and exit.
        10. End of Program.
    
"""


def chat():
    chatbot = RetailChatBot()
    print("Welcome to Otieno Retail Store! We sell shirts, jeans, and hats.")
    for item, quantity in chatbot.stock.items():
        print(f"We have {quantity} {item}(s) available.")

    while True:
        user_input = input("User: ")
        user_input_words = user_input.split()

        if "order" in user_input:
            if len(user_input_words) < 3:
                print("Please format your order like this: order {item} {quantity}")
            else:
                try:
                    item, quantity = user_input_words[1], int(user_input_words[2])
                    print(chatbot.take_order(item, quantity))

                    follow_up = input("Do you want to order something else? (yes/no): ")
                    if follow_up.lower() == "no":
                        print(
                            f"Thank you for purchasing! Your total cost is ${chatbot.get_total_cost()}"
                        )
                        break

                except ValueError:
                    print("The quantity should be a number.")
        else:
            print(chatbot.get_response(user_input))

        if any(word in user_input for word in chatbot.goodbyes):
            break


if __name__ == "__main__":
    chat()
