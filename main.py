from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
OPENAI_API_KEY = "your-api-key-here"
openai.api_key = OPENAI_API_KEY

@app.route('/')
def home():
    return "Welcome to Appfodev CodeBot MVP - AI Code Generator"

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

        return jsonify({"generated_code": generated_code})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
