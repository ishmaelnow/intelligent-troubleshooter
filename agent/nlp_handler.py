# agent/nlp_handler.py with Hugging Face model integration

import json
from sentence_transformers import SentenceTransformer, util

# === Load knowledge base ===
with open('agent/knowledge_base.json', 'r') as f:
    knowledge_base = json.load(f)

# === Load Hugging Face sentence transformer model
semantic_model = SentenceTransformer('all-MiniLM-L6-v2')

# === Diagnostic logic for specific issues ===
def diagnose_network_issue():
    print("Have you restarted your router?")
    response = input("Yes/No: ").strip().lower()
    if response == "no":
        print("➡ Please restart your router and check again.")
    else:
        print("➡ Try resetting your network settings or contacting your internet provider.")

# === Automation logic ===
def automate_fix(issue):
    if issue == "slow_internet":
        print("\n🛠 Automating Fix: Resetting network settings...")
        print("✅ Network settings have been reset. Please check your connection.")
    else:
        print("⚠️ Automation is not available for this issue.")

# === Feedback mechanism ===
def collect_feedback():
    feedback = input("\n🗣️ Did this solution resolve your issue? (Yes/No): ").strip().lower()
    if feedback == "yes":
        print("✅ Great! Your feedback has been recorded.")
    else:
        print("📌 We're sorry the issue persists. We'll improve our solution based on your input.")

# === Map issue keys to diagnostic functions ===
diagnostic_map = {
    "slow_internet": diagnose_network_issue
}

# === Main logic for running the agent ===
def run_agent():
    # Extract symptoms and keys
    symptoms = [entry["symptom"] for entry in knowledge_base.values()]
    keys = list(knowledge_base.keys())

    # Get user input
    user_input = input("Please describe your problem: ")

    # Encode user input and symptoms using Hugging Face model
    user_embedding = semantic_model.encode(user_input, convert_to_tensor=True)
    symptom_embeddings = semantic_model.encode(symptoms, convert_to_tensor=True)

    # Compute semantic similarity
    cos_sim = util.pytorch_cos_sim(user_embedding, symptom_embeddings).squeeze().tolist()

    # Get best match
    best_match_index = cos_sim.index(max(cos_sim))
    best_score = cos_sim[best_match_index]

    if best_score > 0.3:
        matched_key = keys[best_match_index]
        print(f"\n🛠 Identified Issue: {matched_key.replace('_', ' ').title()}")
        print(f"💡 Suggested Solution: {knowledge_base[matched_key]['solution']}")

        # Run diagnostics if available
        if matched_key in diagnostic_map:
            print("\n🔎 Running diagnostic steps...")
            diagnostic_map[matched_key]()

        # Run automated fix
        automate_fix(matched_key)

        # Collect feedback
        collect_feedback()
    else:
        print("❌ Sorry, I couldn't match your issue to any known problems.")
