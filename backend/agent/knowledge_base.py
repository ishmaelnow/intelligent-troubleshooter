import json

# Load the knowledge base from a JSON file
def load_knowledge_base():
    with open("troubleshooting_knowledge_base.json", "r") as f:
        return json.load(f)
