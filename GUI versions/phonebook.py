import tkinter as tk
from tkinter import messagebox

# List to store contacts (as dictionaries)
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Both name and phone number are required!")
        return

    # Adding the contact to the list
    contacts.append({"name": name, "phone": phone})
    update_contact_list()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    messagebox.showinfo("Success", f"Contact {name} added successfully!")

# Function to update the displayed contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Function to search for a contact by name
def search_contact():
    search_name = search_entry.get()
    found = False

    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if search_name.lower() in contact['name'].lower():
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")
            found = True

    if not found:
        messagebox.showinfo("No Results", f"No contacts found for '{search_name}'")

# Function to delete a contact
def delete_contact():
    try:
        selected_contact_index = contact_listbox.curselection()[0]
        selected_contact = contact_listbox.get(selected_contact_index)
        contact_name = selected_contact.split(" - ")[0]

        # Remove the contact from the contacts list
        global contacts
        contacts = [contact for contact in contacts if contact['name'] != contact_name]
        update_contact_list()
        messagebox.showinfo("Success", f"Contact {contact_name} deleted successfully!")
    except IndexError:
        messagebox.showerror("Error", "Please select a contact to delete.")

# Setting up the main window
root = tk.Tk()
root.title("Phonebook")
root.geometry("400x500")

# Entry fields for name and phone number
name_label = tk.Label(root, text="Name:", font=("Helvetica", 12))
name_label.pack(pady=5)
name_entry = tk.Entry(root, font=("Helvetica", 12))
name_entry.pack(pady=5)

phone_label = tk.Label(root, text="Phone Number:", font=("Helvetica", 12))
phone_label.pack(pady=5)
phone_entry = tk.Entry(root, font=("Helvetica", 12))
phone_entry.pack(pady=5)

# Button to add a new contact
add_button = tk.Button(root, text="Add Contact", font=("Helvetica", 12), command=add_contact)
add_button.pack(pady=10)

# Search section
search_label = tk.Label(root, text="Search by Name:", font=("Helvetica", 12))
search_label.pack(pady=5)
search_entry = tk.Entry(root, font=("Helvetica", 12))
search_entry.pack(pady=5)

# Button to search for a contact
search_button = tk.Button(root, text="Search", font=("Helvetica", 12), command=search_contact)
search_button.pack(pady=5)

# Listbox to display contacts
contact_listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=10)
contact_listbox.pack(pady=10)

# Button to delete a selected contact
delete_button = tk.Button(root, text="Delete Contact", font=("Helvetica", 12), command=delete_contact)
delete_button.pack(pady=10)

# Run the main event loop
root.mainloop()
