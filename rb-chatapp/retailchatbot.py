class RetailChatBot:
    """
    A chatbot that simulates a retail store.

    Attributes:
    - greetings (list): A list of strings containing common greetings.
    - goodbyes (list): A list of strings containing common goodbyes.
    - inquiries (list): A list of strings containing common item inquiries.
    - items (dict): A dictionary containing the items and their prices.
    - stock (dict): A dictionary containing the items and their stock levels.
    - total_cost (int): The total cost of the items ordered by the user.

    Methods:
    - take_order(item, quantity): Takes the user's order and updates the stock levels and total cost.
    - get_total_cost(): Returns the total cost of the items ordered by the user.
    - get_response(user_input): Returns a response based on the user's input.
    - chat(): Simulates a conversation with the user.
    """

    def __init__(self):
        self.greetings = ["hi", "hello", "hey"]
        self.goodbyes = ["bye", "goodbye", "see you"]
        self.inquiries = ["how much", "price", "cost"]
        self.items = {"shirt": 20, "jean": 50, "hat": 10}
        self.stock = {"shirt": 100, "jean": 200, "hat": 150}
        self.total_cost = 0

    def take_order(self, item, quantity):
        """
        Takes the user's order and updates the stock levels and total cost.

        Args:
        - item (str): The item ordered by the user.
        - quantity (int): The quantity of the item ordered by the user.

        Returns:
        - str: A message indicating whether the order was successful or not.
        """
        if item.endswith("s"):
            item = item[:-1]
        if item in self.stock and self.stock[item] >= quantity:
            self.stock[item] -= quantity
            self.total_cost += self.items[item] * quantity
            return f"Your order for {quantity} {item}(s) has been placed! We have {self.stock[item]} left."

        else:
            return f"Sorry, we do not have sufficient stock for {item}. We only have {self.stock[item]} left."

    def get_total_cost(self):
        """
        Returns the total cost of the items ordered by the user.

        Returns:
        - int: The total cost of the items ordered by the user.
        """
        return self.total_cost

    def get_response(self, user_input):
        """
        Returns a response based on the user's input.

        Args:
        - user_input (str): The user's input.

        Returns:
        - str: A response based on the user's input.
        """
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
        """
        Simulates a conversation with the user.
        """
        while True:
            user_input = input("User: ")
            if "order" in user_input:
                item, quantity = user_input.split()[1], int(user_input.split()[2])
                print(self.take_order(item, quantity))
            else:
                print(self.get_response(user_input))
            if any(word in user_input for word in self.goodbyes):
                break
