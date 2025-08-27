import re
import csv
import phonenumbers
from phonenumbers import NumberParseException


ADRESS_FILE = './data/contacts.csv'
contacts = []

def is_valid_phone_number(phone_number, region="IR"):
    try:
        parsed_number = phonenumbers.parse(phone_number, region)
        
        if phonenumbers.is_valid_number(parsed_number):
            return True
        
        return False
    except NumberParseException as e:
        return f"Error: {e}"


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def load_contacts():
    try:
        with open(ADRESS_FILE, 'r') as file:
            lines = csv.DictReader(file)
            for line in lines:
                contacts.append(line)
    
    except FileNotFoundError:
        print('This file does not exist.')


def save_contacts():
    try:
        with open(ADRESS_FILE, 'w', newline='') as file:
            field_names = ['Name', 'Phone', 'Email', 'Address']
            writer = csv.DictWriter(file, fieldnames=field_names)
            
            writer.writeheader()
            writer.writerows(contacts)            
    
    except FileNotFoundError:
        print('This file does not exist.')
        
def show_contacts():
    print('Your Address Book')
    for contact in contacts:
        print(f'Name is {contact['Name']}')
        print(f'Phone is {contact['Phone']}')
        print(f'Email is {contact['Email']}')
        print(f'Address is {contact['Address']}')
        
        print('-' * 35)
    

def add_contacts():
    print('Add New Contact: ')
    name = input('Enter Name: ').strip()
    phone = input('Enter Phone: ').strip()
    email = input('Enter Email: ').strip()
    address = input('Enter Address: ').strip()
    
    if not is_valid_phone_number(phone):
        raise ValueError('Phone number must be numeric.')
    if not is_valid_email(email):
        raise ValueError('The email format you entered is invalid. Please try again.')
    
    contact = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Address': address,
    }
    contacts.append(contact)
    save_contacts()
    print(f'{name} has been added to your address book.')

def update_contact():
    print('Update Contact')
    phone = input('Enter the phone number of the contact to update: ')
    if not is_valid_phone_number(phone):
        raise ValueError('The number foramt you entered is invalid. Please try again.')
    for contact in contacts:
        if contact['Phone'] == phone:
            print(f'Current Details for {contact['Name']}: ')
            print(f'Name is {contact['Name']}')
            print(f'Phone is {contact['Phone']}')
            print(f'Email is {contact['Email']}')
            print(f'Address is {contact['Address']}')
            print('-' * 35)
            

            new_name = input('New Name (Press Enter to keep current): ').strip()
            new_email = input('New Email (Press Enter to keep current): ').strip()
            new_address = input('New Address (Press Enter to keep current): ').strip()
            
            if new_name:
                contact['Name'] = new_name
            if new_email:
                contact['Email'] = new_email
            if new_address:
                contact['Address'] = new_address
            
            save_contacts()
            print(f'Current Details for {contact['Name']} have been updated.')
            return
    
    print('Contact Not Found.')
    
def delet_contact():
    print('Delete Contact')
    phone = input('Enter the phone number of the contact to delete: ')
    if not is_valid_phone_number(phone):
        raise ValueError('The number foramt you entered is invalid. Please try again.')
    
    for contact in contacts:
        if contact['Phone'] == phone:
            deleted_name = contact['Name']
            contacts.remove(contact)
            save_contacts()
            print(f'{deleted_name} has been deleted from your address book.')
            return
    print('Contact Not Found.')