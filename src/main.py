from utills import (load_contacts, update_contact, 
                     add_contacts, delet_contact ,show_contacts)
    
load_contacts()
while True:
    try:
        print()
        print('Address Book Menu:')
        print('1. Add Contact')
        print('2. View Contacts')
        print('3. Update Contact')
        print('4. Delete Contact')
        print('5. Exit')
        
        choice = int(input('Enter your choice (1/2/3/4/5): ').strip())

        if choice == 1:
            add_contacts()
        elif choice == 2:
            show_contacts()
        elif choice == 3:
            update_contact()
        elif choice ==4:
            delet_contact()
        elif choice == 5:
            print('Goodbye!')
            exit()
        else:
            print('Invalid choice, Please try again!')
                
    except Exception as e:
        print(f'Error: {e}')
    