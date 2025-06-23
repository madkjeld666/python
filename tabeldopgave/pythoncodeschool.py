import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("Customer Data")

# Create a Treeview widget
table = ttk.Treeview(app)

# Define the columns
table['columns'] = ('Name', 'Email', 'Phone', 'Address')

# Format the columns
table.column('#0', width=0, stretch=tk.NO)
table.column('Name', anchor=tk.W, width=150)
table.column('Email', anchor=tk.W, width=200)
table.column('Phone', anchor=tk.W, width=150)
table.column('Address', anchor=tk.W, width=150)

# Create the headings
table.heading('#0', text='', anchor=tk.W)
table.heading('Name', text='Name', anchor=tk.W)
table.heading('Email', text='Email', anchor=tk.W)
table.heading('Phone', text='Phone', anchor=tk.W)
table.heading('Address', text='Address', anchor=tk.W)

# Sample data
data = [
    ('John Smith', 'john@example.com', '(555) 123-4567', 'Vijverstraat 5'),
    ('Emily Johnson', 'emily@example.com', '(555) 987-6543', 'Hoofdstraat 11'),
    ('Michael Davis', 'michael@example.com', '(555) 246-8135', 'Droogstraat 7')
]

# Configure alternating row colors
table.tag_configure('oddrow', background='#FF0000')
table.tag_configure('evenrow', background='#00FF00')

# Add data with alternating row colors
for i in range(len(data)):
    if i % 2 == 0:
        table.insert(parent='', index=i, values=data[i], tags=('evenrow',))
    else:
        table.insert(parent='', index=i, values=data[i], tags=('oddrow',))

# Pack the table
table.pack(expand=True, fill=tk.BOTH)

app.mainloop()