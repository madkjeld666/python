import tkinter as tk
import json
import requests

# route die word opgestuurd
route = {
    "start": "C1.13",
    "eind": "C1.06",
    "tussenstop": ["C1.04"]
}

def stuur_route_naar_server():
    url = "http://localhost:5000/upload"
    try:
        response = requests.post(url, json=route)
        print("Verzonden:", response.json())
    except Exception as e:
        print("Fout bij verzenden:", e)

# Tkinter-venster
root = tk.Tk()
root.title("Routeplanner")

label = tk.Label(root, text="Route wordt verzonden bij afsluiten.")
label.pack(padx=20, pady=20)

# Voordat het venster sluit, upload de route
def afsluiten():
    stuur_route_naar_server()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", afsluiten)

root.mainloop()
