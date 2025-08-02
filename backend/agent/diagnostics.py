from agent.knowledge_base import load_knowledge_base

def diagnose_network_issue(user_input):
    knowledge_base = load_knowledge_base()
    user_input = user_input.lower()  # Ensure matching is case-insensitive

    # Match keywords to solutions
    if "restart" in user_input:
        return knowledge_base["restart_router"]
    elif "cable" in user_input or "plug" in user_input:
        return knowledge_base["check_cables"]
    elif "reset" in user_input or "settings" in user_input:
        return knowledge_base["reset_network_settings"]
    elif "browser" in user_input or "cache" in user_input:
        return knowledge_base["clear_cache"]
    elif "internet" in user_input or "isp" in user_input:
        return knowledge_base["isp_contact"]
    elif "wifi" in user_input or "signal" in user_input:
        return knowledge_base["check_wifi_signal"]
    elif "firewall" in user_input or "security" in user_input:
        return knowledge_base["disable_firewall"]
    elif "firmware" in user_input or "update" in user_input:
        return knowledge_base["update_firmware"]
    elif "dns" in user_input:
        return knowledge_base["check_dns_settings"]
    elif "reboot" in user_input or "restart device" in user_input:
        return knowledge_base["reboot_device"]
    elif "network" in user_input or "connection" in user_input:
        # General network issue fallback tip
        return "It seems like a network issue. " + knowledge_base["check_wifi_signal"]
    else:
        # Fallback with multiple tips
        fallback = [
            knowledge_base["restart_router"],
            knowledge_base["check_cables"],
            knowledge_base["check_wifi_signal"]
        ]
        return "Sorry, I couldn't determine the issue. Here are some things to try:\n- " + "\n- ".join(fallback)
# This function provides diagnostic solutions based on user input related to network issues.
# It uses a knowledge base to match keywords and return appropriate troubleshooting steps.