
from agent.diagnostics import diagnose_network_issue
from agent.fix_automation import automate_fix

def main():
    print("Welcome to the Intelligent Troubleshooting Agent.")
    print("Please describe your issue below:")

    user_input = input(">> ").strip().lower()

    if "network" in user_input or "internet" in user_input:
        diagnose_network_issue()

        automate = input("Would you like me to try an automated fix? (Yes/No): ").strip().lower()
        if automate == "yes":
            automate_fix("network_issue")
    else:
        print("Sorry, I couldn't understand your issue.")
        print("Please try describing a network-related problem.")

if __name__ == "__main__":
    main()
=======
# main.py

from agent import nlp_handler

if __name__ == "__main__":
    # Simply triggers the agent’s conversation flow
    nlp_handler.run_agent()

