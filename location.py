# main_script.py
from tkinter import *
import tkinter as tk
import phonenumbers
# from phonenum_location import number
from phonenumbers import geocoder, carrier
# number="+91 9326544271"
# Parse the phone number for country information
def get_phone_info():
    # Get phone number from the entry widget
    
    number = entry.get()
    # Parse the phone number for country information
    ch_number = phonenumbers.parse(number, "CH")
    country_info = geocoder.description_for_number(ch_number, "en")
    country_label.config(text="Country: " + country_info)

    # Parse the phone number for carrier information
    service_number = phonenumbers.parse(number, "RO")
    carrier_info = carrier.name_for_number(service_number, "en")
    carrier_label.config(text="Carrier: " + carrier_info)
# Create the main window

root = tk.Tk()
root.geometry("500x300")
root.title("Phone Number Info")

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

note=tk.Label(text="note: please enter number in these format: eg :+91 9876533567",height=200)
note.pack()

# Run the Tkinter event loop
root.mainloop()
