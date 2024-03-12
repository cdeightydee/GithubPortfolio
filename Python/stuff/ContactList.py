import json

def save_contact(contact: dict, filename: str):
    with open(filename, "a") as f:
        json.dump(contact, f)

print("This program saves a Contact in you Contacts List")
name = input("Contact name? ")
email = input("Contact em  ail? ")
phone = input("Contact phone? ")
relationship = input("Contact relationship? ")
contact = {
    "name": name,
    "email": email,
    "phone": phone,
    "relationship": relationship
}
save_contact(contact, "contact.json")
