def automate_fix(issue, return_output=False):
    if issue == "network_issue":
        result = "Attempting to reset your network settings automatically...\nNetwork settings have been reset. Please check your connection."
    else:
        result = "Automatic fix is not available for this issue."

    if return_output:
        return result
    else:
        print(result)
