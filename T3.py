import re

def check_password_complexity(password):
    # Define complexity requirements
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_lowercase = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special_char = re.search(r'[@$!%*?&]', password) is not None

    # Check if password meets all criteria
    if (len(password) >= min_length and 
        has_uppercase and 
        has_lowercase and 
        has_digit and 
        has_special_char):
        return "Password is strong."
    else:
        return "Password is weak. It must meet the following criteria:\n" + \
               f"- At least {min_length} characters long\n" + \
               "- At least one uppercase letter\n" + \
               "- At least one lowercase letter\n" + \
               "- At least one digit\n" + \
               "- At least one special character (e.g., @$!%*?&)"

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password to check its complexity: ")
    result = check_password_complexity(user_password)
    print(result)
