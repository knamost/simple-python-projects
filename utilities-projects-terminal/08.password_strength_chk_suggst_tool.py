"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""




import string
import random
import getpass

#   password strengh checker
def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Too short (minimum 8 characters)")
        
    if not any(c.islower() for c in password):
        issues.append("Missing lower case letter.")
        issues.append("Too short (minimum 8 characters)")
        
    if not any(c.isupper() for c in password):
        issues.append("Missing upper case letter.")
        
    if not any(c.isdigit() for c in password):
        issues.append("Missing Digit.")
        
    if not any(c in string.punctuation for c in password):
        issues.append("Missing special character (e.g., @, #, $, etc.)")
        
    return issues

#   Password suggestion tool (random password generators)
def strong_password_suggestion(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))
    

password = getpass.getpass("Enter a password: ")
issues = check_password_strength(password)
if not issues:
    print("Strong password!, you're good to go....")
else:
    ("You got weak password")
    for issue in issues:
        print(f"- {issue}")

print("\n Suggesting you a strong password")
print(strong_password_suggestion())
