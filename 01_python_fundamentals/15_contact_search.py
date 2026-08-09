# A program to store contacts in a dictionary and search for a phone number using .get().

contacts = {}

for i in range(1 , 4):
    name = input(f"Enter contact {i} name: ")
    phone_number = input(f"Enter contact {name}'s phone number: ")
    contacts[name] = phone_number

search_name = input("Enter the name of the contact you want to search for: ")
phone_number = contacts.get(search_name)

if phone_number is None:
    print(f"{search_name} not found in contacts.")

else:
    print(f"{search_name}'s phone number is: {phone_number}")

print(f"All contacts: {contacts}")

