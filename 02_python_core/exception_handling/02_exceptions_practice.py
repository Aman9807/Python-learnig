# Topic: Advanced Exception Handling Practice (Month 2: Core Python)
#
# Key Concepts to Practice:
# 1. KeyError     : Occurs when searching for a dictionary key that doesn't exist.
# 2. IndexError   : Occurs when accessing a list index that is out of bounds.
# 3. ValueError   : Occurs when converting invalid text to numbers.
# 4. `try-except-else-finally` flow in real-world scenarios.

# ====================================================
# PRACTICE TASKS:
# ====================================================

# Task 1: Safe Dictionary Lookup (`safe_get_user_role`)
def safe_get_user_role(username):
    user_roles = {"aman": "Admin", "priya": "Developer", "rahul": "Tester"}
    try:
        role = user_roles[username.lower()]
    except KeyError:
        print(f"❌ Error: User '{username}' was not found in the database!")
    else:
        print(f"✅ User '{username}' has role: {role}")

# Task 2: Safe List Element Access (`safe_get_fruit`)
def safe_get_fruit(index):
    fruits = ["Apple", "Banana", "Cherry", "Mango"]
    try:
        fruit = fruits[index]
    except IndexError:
        print(f"❌ Error: Index {index} is out of range! (Valid index: 0 to {len(fruits)-1})")
    except TypeError:
        print("❌ Error: Index must be an integer number!")
    else:
        print(f"✅ Fruit at index {index}: {fruit}")
    finally:
        print("--- Fruit check complete ---")

# Task 3: Safe Age Calculator (`safe_calculate_birth_year`)
def safe_calculate_birth_year(age_input):
    current_year = 2026
    try:
        age = int(age_input)
        birth_year = current_year - age
    except ValueError:
        print(f"❌ Error: '{age_input}' is not a valid numeric age!")
    else:
        print(f"✅ Your birth year is approximately {birth_year}")
    finally:
        print("--- Age check complete ---")

# Execution Test Calls
safe_get_fruit(1)
safe_get_fruit(7)
safe_get_user_role("Rahul")
safe_calculate_birth_year("26")
