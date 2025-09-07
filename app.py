from chat_engine import chat_with_person
from memory_loader import load_memories_from_folder
from memory_store import MemoryStore
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load memory only once
text = load_memories_from_folder("assets")
store = MemoryStore()
store.add_memory(text)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = chat_with_person(user_input, store)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)