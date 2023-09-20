# Simplified Python Retail Chatbot

## Description
Retail Chatbot is a Python-based application, which helps to automate conversation with customers, provide product price information, receive orders for items, update the available stock, and calculate the total order cost.

## How to use it

To initiate interaction with the chatbot, run `chat.py` script:

```bash
> python chat.py
```

Now, you can converse with the chatbot in the terminal, asking for prices for different items:

```
User: How much is a shirt?
Chatbot: The price of the shirt is $20.
To place an order for an item, use the following command: "order [item_name] [quantity]", where item_name is the item you wish to purchase and quantity is the number of that item you wish to buy.
``````
For example:

```
User: order shirt 2
Chatbot: Your order for 2 shirt(s) has been placed! We have 98 left.
The total cost of the ordered items will be calculated, and you will get an update about the number of remaining items.
```

After placing all the orders, answer negatively to the additional ordering proposal:

```
User: no
Chatbot: Thank you for purchasing! Your total cost is $40.
Contributing
To contribute to this application, fork this repository, create your branch, commit your changes to the new branch, and open a pull request in this repository.
```

## License
This project is licensed under the MIT License.

You should definitely adapt this boilerplate to fit the specifics of your own project.