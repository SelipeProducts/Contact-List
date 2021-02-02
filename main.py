import csv

class contact:
  name = ""
  address = "" 
  phone_number = ""
  email_address = ""

  def __init__(self, name, address, phone_number, email_address):   
    self.name = name
    self.address = address
    self.phone_number = phone_number
    self.email_address = email_address

  # getter method for name
  def get_name(self): 
      return self.name
  # setter method for name
  def set_name(self, x): 
      self.name = x 
  
  # getter method for address
  def get_address(self): 
      return self.address
  # setter method for address
  def set_address(self, x): 
      self.address = x 
  
  # getter method for email_address
  def get_phone_number(self): 
      return self.phone_number
  # setter method for email_address
  def set_phone_number(self, x): 
      self.phone_number = x 

  # getter method for email_address
  def get_email_address(self): 
      return self.email_address
  # setter method for email_address
  def set_email_address(self, x): 
      self.email_address = x 

class contact_book:
  contact_list = []
  def __init__(self, contact_list):   
    self.contact_list = contact_list
  
  # getter method for contact_list
  def get_contact_list(self): 
      return self.contact_list
  # setter method for contact_list
  def set_contact_list(self, x): 
      self.contact_list = x

  def print_contacts(self):
    contacts = self.get_contact_list()
    for i in range(0, len(contacts)):
      contact_name = contacts[i].get_name()
      contact_address = contacts[i].get_address()
      contact_phone_number = contacts[i].get_phone_number()
      contact_email = contacts[i].get_email_address()

      print(str(i+1)+ ")", contact_name, contact_address, contact_phone_number, contact_email,"\n")


  def print_single_contact(self, sing_contact, iteration):
    contact_name = sing_contact.get_name()
    contact_address = sing_contact.get_address()
    contact_phone_number = sing_contact.get_phone_number()
    contact_email = sing_contact.get_email_address()
    print(iteration, contact_name, contact_address, contact_phone_number, contact_email)

  def search_contacts(self):
    contacts = self.get_contact_list()
    search_input = input("\nSearch: ")
    did_match = False

    for i in range(0, len(contacts)):
      contact_name = contacts[i].get_name()
      contact_address = contacts[i].get_address()
      contact_phone_number = contacts[i].get_phone_number()
      contact_email = contacts[i].get_email_address()
      if search_input in contact_name or search_input in contact_address or search_input in contact_email or search_input in str(contact_phone_number):
        print("Sucessful Match\n")
        self.print_single_contact(contacts[i], i+1)
        did_match = True
    if did_match == False:
        print("No Matches.\n")
  
  def add_contact(self):
    list_contact = self.get_contact_list()
    print("\nAdding Contact")
    add_name = input("Name: ")
    add_address = input("Address: ")
    add_phone_num = input("Phone Number: ")
    add_email = input("Email:")

    added_contact = contact(add_name, add_address, add_phone_num, add_email)
    list_contact.append(added_contact)
    self.set_contact_list(list_contact)
    print("\nAdded Contact: ")
    self.print_single_contact(added_contact, 1)
    print()

    self.add_contact_and_write_file("contacts.csv", added_contact)

  def remove_contact(self): 
    list_contact = self.get_contact_list()
    print("\nRemoving Contact")
    print("Select from numbered list")
    self.print_contacts()
    remove_index = input("Contact Number: ")
    remove_index = int(remove_index)
    remove_index -= 1
    print("Removed Contact")
    self.print_single_contact(list_contact[remove_index], 1)

    self.remove_contact_and_edit_file("contacts.csv", list_contact[remove_index])


    del list_contact[remove_index]
    self.set_contact_list(list_contact)
    print("\nRemaining Contacts")
    self.print_contacts()

  
  def edit_contact(self):
    list_contact = self.get_contact_list()
    print("\nEditing Contact")
    print("Select from numbered list")
    self.print_contacts()
    edit_index = input("Contact Number: ")
    edit_index = int(edit_index)
    edit_index -= 1
    print("Are you sure you want to edit this Contact?")
    self.print_single_contact(list_contact[edit_index], 1)

    old_contact = list_contact[edit_index]

    confirm_choice = input("Y/N: ")
    if(confirm_choice == "y" or confirm_choice == "Y" or confirm_choice == "1"):
      print("\nEdit Details")
      edit_name = input("Name: ")
      edit_address = input("Address: ")
      edit_phone_num = input("Phone Number: ")
      edit_email = input("Email:")

      edited_contact = contact(edit_name, edit_address, edit_phone_num, edit_email)
      print("\nEdited Contact: ")
      self.print_single_contact(edited_contact, 1)
      list_contact[edit_index] = edited_contact
      self.set_contact_list(list_contact)
      print()

      self.edit_contact_and_edit_file("contacts.csv", old_contact, edited_contact)
  
  def read_file_and_fill_list(self, file):
      with open(file, 'r') as myFile:
        lines = csv.reader(myFile, delimiter=',')
        for line in lines:
          file_name = line[0]
          #print("Print:",file_name)
          file_address = line[1]
          file_phone = line[2]
          file_email = line[3]

          file_contact = contact(file_name, file_address, file_phone, file_email)
          
          list_contact = self.get_contact_list()
          list_contact.append(file_contact)
          self.set_contact_list(list_contact)

  def add_contact_and_write_file(self, file, contact):
    the_contact = contact
    the_contact_name = the_contact.get_name()
    the_contact_address = the_contact.get_address()
    the_contact_phone = the_contact.get_phone_number()
    the_contact_email = the_contact.get_email_address()
    with open(file, mode='a') as the_file:
      the_writer = csv.writer(the_file, delimiter=',')
      the_writer.writerow([the_contact_name, the_contact_address, the_contact_phone, the_contact_email])

  def remove_contact_and_edit_file(self, file, contact):
      lines = list()
      
      the_contact = contact
      the_contact_name = the_contact.get_name()
      the_contact_address = the_contact.get_address()
      the_contact_phone = the_contact.get_phone_number()
      the_contact_email = the_contact.get_email_address()

      with open(file, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
          lines.append(row)
          check_name = row[0]
          check_address = row[1]
          check_phone = row[2]
          check_email = row[3]
          
          if(check_name == the_contact_name and check_address == the_contact_address and check_phone == the_contact_phone and check_email == the_contact_email):
            lines.remove(row)

      with open(file, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
  
  def edit_contact_and_edit_file(self, file, old_contact, new_contact):
    lines = list()
      
    the_contact = old_contact
    the_contact_name = the_contact.get_name()
    the_contact_address = the_contact.get_address()
    the_contact_phone = the_contact.get_phone_number()
    the_contact_email = the_contact.get_email_address()

    new_contact = new_contact
    new_contact_name = new_contact.get_name()
    new_contact_address = new_contact.get_address()
    new_contact_phone = new_contact.get_phone_number()
    new_contact_email = new_contact.get_email_address()

    with open(file, 'r') as readFile:
      reader = csv.reader(readFile)
      i = 0
      for row in reader:
        lines.append(row)
        check_name = row[0]
        check_address = row[1]
        check_phone = row[2]
        check_email = row[3]
        
        if(check_name == the_contact_name and check_address == the_contact_address and check_phone == the_contact_phone and check_email == the_contact_email):
          #lines.remove(row) since nEditing
          #writer.writerow(row)
          #print(lines)
          lines[i] = [new_contact_name, new_contact_address, new_contact_phone, new_contact_email]
          #lines = [new_contact_name, new_contact_address, new_contact_phone, new_contact_email]
        i += 1



    with open(file, 'w') as writeFile:
      writer = csv.writer(writeFile)
      writer.writerows(lines)


def main():
  contact_cesarlopez = contact("Cesar Lopez", "431 Carver St. Chula Vista, CA 91911", 6193701017, "cesarlopez20@yahoo.com")

  contact_martinmartin = contact("Martin Martin", "1951 E Valley Pkwy, Escondido, CA 92027", 7608801839, "m3martin@ucsd.edu")

  my_contact = [contact_cesarlopez, contact_martinmartin]
  my_contact_book = contact_book(my_contact)

  my_contact_book.read_file_and_fill_list("contacts.csv")

  gamerunning = True
  while gamerunning == True:
    print("My Contact Book")
    print("1) Print Contacts\n2) Search Contacts\n3) Add Contacts\n4) Remove Contacts\n5) Edit Contacts\n6) Read CSV and Fill Contacts\n7) Exit")
    choice = input("Choice: ")
    choice = int(choice)
    if choice == 1:
      print("\nPrinted Contacts")
      my_contact_book.print_contacts()
    elif choice == 2:
      my_contact_book.search_contacts()
    elif choice == 3:
      my_contact_book.add_contact()
    elif choice == 4:
      my_contact_book.remove_contact()
    elif choice == 5:
      my_contact_book.edit_contact()
    elif choice == 6:
      my_contact_book.read_file_and_fill_list("contacts.csv")
      print()
    else:
      break
    
main()

#Note: watch out with matching numbers to string input

#Note: Make sure csv file has no blank lines at the end of it