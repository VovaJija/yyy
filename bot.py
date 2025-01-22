from flask import Flask, request, jsonify

app = Flask(__name__)

# Словарь ответов
RESPONSES = {
    "привет": "Привет! Чем могу помочь?",
    "как дела": "У меня все отлично! Спасибо, что спросили.",
    "помощь": "Вот список команд, которые я понимаю: привет, как дела, помощь.",
}

@app.route('/mattermost', methods=['POST'])
def handle_message():
    data = request.json
    user_message = data.get('text', '').lower()

    # Поиск ответа
    response = RESPONSES.get(user_message, "Извините, я не понимаю этот запрос.")
    
    return jsonify({"text": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
