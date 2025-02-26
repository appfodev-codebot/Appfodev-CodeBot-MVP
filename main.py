from flask import Flask, request, jsonify
import openai
from pymongo import MongoClient

app = Flask(__name__)

# OpenAI API Key
OPENAI_API_KEY = "your-api-key-here"
openai.api_key = OPENAI_API_KEY

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["codebot_db"]
collection = db["generated_codes"]

@app.route('/generate-code', methods=['POST'])
def generate_code():
    data = request.json
    user_prompt = data.get("prompt", "")

    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Write a code snippet for: {user_prompt}"}]
        )
        generated_code = response["choices"][0]["message"]["content"]

        # Save to MongoDB
        collection.insert_one({"prompt": user_prompt, "generated_code": generated_code})

        return jsonify({"generated_code": generated_code})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/history', methods=['GET'])
def get_history():
    history = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB object ID
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)
