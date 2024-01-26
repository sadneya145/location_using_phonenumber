from tkinter import *
import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier

def get_phone_info():
    # Get phone number from the entry widget
    number = entry.get()

    try:
        # Parse the phone number for country information
        ch_number = phonenumbers.parse(number, "CH")
        country_info = geocoder.description_for_number(ch_number, "en")
        country_label.config(text="Country: " + country_info)

        # Parse the phone number for carrier information
        service_number = phonenumbers.parse(number, "RO")
        carrier_info = carrier.name_for_number(service_number, "en")
        carrier_label.config(text="Carrier: " + carrier_info)
    except phonenumbers.NumberFormatException:
        # Handle invalid phone number
        messagebox.showerror("Invalid Number", "Please enter a valid phone number")
        country_label.config(text="Country: ")
        carrier_label.config(text="Carrier: ")

# Create the main window
root = tk.Tk()
root.title("Phone Number Info")
root.geometry('500x500')

# Create entry widget for phone number
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create button to get phone info
button = tk.Button(root, text="Get Phone Info", command=get_phone_info)
button.pack(pady=10)

# Labels to display country and carrier information
country_label = tk.Label(root, text="Country: ")
country_label.pack()

carrier_label = tk.Label(root, text="Carrier: ")
carrier_label.pack()

# Run the Tkinter event loop
root.mainloop()
