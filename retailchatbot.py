class RetailChatBot:
    def __init__(self):
        self.greetings = ["hi", "hello", "hey"]
        self.goodbyes = ["bye", "goodbye", "see you"]
        self.inquiries = ["how much", "price", "cost"]
        self.items = {"shirt": 20, "jean": 50, "hat": 10}
        self.stock = {"shirt": 100, "jean": 200, "hat": 150}
        self.total_cost = 0

    def take_order(self, item, quantity):
        if item.endswith("s"):
            item = item[:-1]
        if item in self.stock and self.stock[item] >= quantity:
            self.stock[item] -= quantity
            self.total_cost += self.items[item] * quantity
            return f"Your order for {quantity} {item}(s) has been placed! We have {self.stock[item]} left."

        else:
            return f"Sorry, we do not have sufficient stock for {item}. We only have {self.stock[item]} left."

    def get_total_cost(self):
        return self.total_cost

    def get_response(self, user_input):
        # Convert user input to lowercase
        user_input = user_input.lower()

        # Greeting
        if any(word in user_input for word in self.greetings):
            return "Hello! How can I assist you today?"
        # Goodbye
        elif any(word in user_input for word in self.goodbyes):
            return "Goodbye! Have a great day!"

        # Item inquiries
        elif any(inquiry in user_input for inquiry in self.inquiries):
            for item, price in self.items.items():
                if item in user_input:
                    return f"The price of the {item} is ${price}."

            return "I'm sorry, I don't have information on that item."

        # General Help
        elif "help" in user_input:
            return (
                "You can ask about the prices of our items like shirts, jeans, or hats."
            )
        else:
            return "I'm sorry, I didn't understand that."

    # Add chat method
    def chat(self):
        while True:
            user_input = input("User: ")
            if "order" in user_input:
                item, quantity = user_input.split()[1], int(user_input.split()[2])
                print(self.take_order(item, quantity))
            else:
                print(self.get_response(user_input))
            if any(word in user_input for word in self.goodbyes):
                break
