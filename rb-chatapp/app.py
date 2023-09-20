from flask import Flask, request, jsonify, render_template, session
from flask import redirect, url_for
from retailchatbot import RetailChatBot
import threading

app = Flask(__name__)
app.secret_key = "23243432"  # Set your secret key
bot = RetailChatBot()
lock = threading.Lock()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        with lock:
            if "order" in user_input.lower():
                item, quantity = user_input.split()[1], int(user_input.split()[2])
                response = bot.take_order(item, quantity)
            else:
                response = bot.get_response(user_input)
        # Store messages conversations in session
        messages = session.get("messages", [])
        messages.append({"sender": "User", "text": user_input})
        messages.append({"sender": "Bot", "text": response})
        session["messages"] = messages
    else:
        messages = session.get("messages", [])
    return render_template("index.html", messages=messages)


@app.route("/reset", methods=["POST"])
def reset():
    global bot
    bot = RetailChatBot()
    session.pop("messages", None)  # clear the messages when restarting
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
