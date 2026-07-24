# Password Strength Checker
while True:

 password = input("\n \n Enter Password: ")

# Check conditions
 has_upper = any(char.isupper() for char in password)
 has_lower = any(char.islower() for char in password)
 has_digit = any(char.isdigit() for char in password)

 symbols = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
 has_symbol = any(char in symbols for char in password)

# Calculate score
 score = 0

 if len(password) >= 8:score += 1

 if has_upper:score += 1

 if has_lower:score += 1

 if has_digit:score += 1

 if has_symbol:score += 1

# Determine strength
 if score <= 2:
    strength = "Weak"
 elif score <= 4:
    strength = "Medium"
 else:
    strength = "Strong"

# Display result
 print("\nPassword Analysis")
 print("-----------------")
 print(f"Length: {len(password)}")
 print(f"Contains Uppercase: {has_upper}")
 print(f"Contains Lowercase: {has_lower}")
 print(f"Contains Digit: {has_digit}")
 print(f"Contains Symbol: {has_symbol}")

 print(f"\nPassword Strength: {strength}")

# Suggestions
 print("\nSuggestions:")

 if len(password) < 8:
    print("- Use at least 8 characters")

 if not has_upper:
    print("- Add uppercase letters")

 if not has_lower:
    print("- Add lowercase letters")

 if not has_digit:
    print("- Add numbers")

 if not has_symbol:
    print("- Add special characters")

 if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_symbol
):
    print("- Excellent password!")
 while True:
        choice = input("\nCheck another password? (y/n): ").lower()

        if choice == "y":
            break  

        elif choice == "n":
            print("Exiting Password Checker...")
            exit() 

        else:
            print("Please enter only y or n.")
   
   