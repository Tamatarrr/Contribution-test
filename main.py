def check_strength(password):
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Strong password"
    elif score >= 3:
        return "Medium password"
    else:
        return "Weak password"

pwd = input("Enter a password: ")
print(check_strength(pwd))
