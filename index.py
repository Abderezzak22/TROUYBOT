from flask import Flask, render_template, request
from dotenv import load_dotenv
from domain_layer import get_response
from presentation_layer import bot

load_dotenv()  # Load environment variables

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        update = request.get_json()  # Get JSON data from request
        handle_message(update)
        return "ok"
    return render_template("status.html")

def handle_message(update):
    message = update.get('message')
    if message:
        chat_id = message['chat']['id']
        text = message.get('text')
        if text:
            response = get_response(text)
            bot.send_message(chat_id=chat_id, text=response.text)

if __name__ == "__main__":
    app.run(debug=True)
