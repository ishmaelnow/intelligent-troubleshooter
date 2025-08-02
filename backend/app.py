from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# === Load environment variables from .env ===
load_dotenv()

# === Flask App Setup ===
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

# === Enable CORS for cross-origin requests ===
CORS(app)

# === Import AI diagnostic logic ===
from agent.diagnostics import diagnose_network_issue
from agent.fix_automation import automate_fix

# === Routes ===
@app.route("/diagnose", methods=["POST"])
def diagnose():
    data = request.json
    user_input = data.get("message", "").lower()
    response = diagnose_network_issue(user_input)
    return jsonify({"response": response})

@app.route("/automate", methods=["POST"])
def automate():
    data = request.json
    issue = data.get("issue", "network_issue")
    result = automate_fix(issue, return_output=True)
    return jsonify({"response": result})

# === App Runner ===
if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_ENV') == 'development')
